#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from zipfile import ZipFile

from services.xmind_parser.node import Node
from services.xmind_parser.node_type import NodeType
from services.exceptions import DTreeValidationError, DTreeProgrammingError

TEST_DIR_NAME = "data/"
XMIND_TEST_FILE = "example_a_verifier.xmind"


class DTree:
    def __init__(self, filename=XMIND_TEST_FILE, dir_name=TEST_DIR_NAME, from_memory=None):
        self.filename = filename
        self.dir_name = dir_name
        self.input_zip = from_memory if from_memory else DTree.__extract_zip_from_file(dir_name + filename)
        self.raw_json_data = DTree.__extract_zip(self.input_zip)
        self.nodes = []
        # NOTE: Doesn't handle multiple rootTopic
        self.__populate_node(self.raw_json_data[0]["rootTopic"])
        if "relationships" in self.raw_json_data[0]:
            self.__complete_relationships(self.raw_json_data[0]["relationships"])
        self.__check_errors()

    def __repr__(self):
        nodes = ""
        for i in range(len(self.nodes)):
            nodes += f"{self.nodes[i]}\n\n"
        return f"DTree from {self.dir_name}{self.filename}\n\n{nodes}"

    @staticmethod
    def __extract_zip_from_file(filename):
        # TODO: Error managment, wrong file
        return ZipFile(filename)

    @staticmethod
    def __extract_zip(input_zip):
        # TODO: Error managment, wrong file
        json_bytes = input_zip.read("content.json")
        json_data = json.loads(json_bytes.decode('utf-8'))
        return json_data

    def __populate_node(self, data):
        try:
            node = Node(node_id=data["id"],
                        title=data["title"],
                        description=data.get("notes", {}),
                        style=data.get("style", {}))
            if "href" in data:
                node.set_href(data["href"])
        except KeyError as err:
            raise DTreeProgrammingError(f"Can't initialize node ({err})", f"Id: {data.get('id')}")
        
        self.__add_children(node, data)
        self.nodes.append(node)
        return node

    def __add_children(self, node, data):
        children = []
        if "children" in data:
            children = [self.__populate_node(c) for c in data["children"]["attached"]]
        
            if "summary" in data["children"]:
                summaries = [self.__populate_node(summary) for summary in data["children"]["summary"]]
                # Set up summary only for children with no existing children
                # NOTE: if summary encompasses more than 1 columns of children it doesn't work
                valid_children = (c for c in children if len(c.children) == 0)
                for child in valid_children:
                    for summary in summaries:
                        child.add_child(summary)
            
            if "detached" in data["children"]:
                for detached in data["children"]["detached"]:
                    self.__populate_node(detached)

        for child in children:
            node.add_child(child)

    def __complete_relationships(self, relationships):
        for relation in relationships:
            try:
                node_id = relation['id']
                start_node = self.get_node(relation['end1Id'])
                end_node = self.get_node(relation['end2Id'])
            except KeyError as err:
                raise DTreeProgrammingError(f"Can't initialize relation ({err})")
            
            if not start_node.has_links and len(start_node.children) != 0:
                # TODO: Set up warnings logs
                start_node.children = []
            start_node.has_links = True

            has_title = "title" in relation
            if has_title and start_node.type in [NodeType.QUESTION, NodeType.STEP]:
                node = Node(node_id, relation.get("title"), node_type=NodeType.ANSWER)
                start_node.add_child(node)
                node.add_child(end_node)
                self.nodes.append(node)
            elif not has_title and start_node.type not in [NodeType.UNDEFINED, NodeType.ATTACHEMENT, NodeType.EXTERNAL_LINK]:
                start_node.add_child(end_node)
            else:
                raise DTreeValidationError(f"Can't initialize relation between:\n----\n{start_node}\n---\nand\n----\n{end_node}\n----\n")


    def __check_errors(self):
        node_ids = [node.id for node in self.nodes]
        if len(node_ids) != len(set(node_ids)):
            raise DTreeProgrammingError(f"Duplicate node_ids !")
        for node in self.nodes:
            node.check_errors()

        nodes = [node for node in self.nodes if node.type == NodeType.APP_NAME]
        if len(nodes) == 0:
            raise DTreeValidationError(f"Need one {NodeType.APP_NAME} node")
        elif len(nodes) > 1:
            raise DTreeValidationError(f"Only one {NodeType.APP_NAME} is accepted", f"{[n for n in nodes]}")


    def get_node(self, node_id):
        for i in range(len(self.nodes)):
            if self.nodes[i].id == node_id:
                return self.nodes[i]
        raise DTreeProgrammingError(f"Can't find node", f"Id: {node_id}")

    def get_root_node(self):
        for i in range(len(self.nodes)):
            if self.nodes[i].type == NodeType.APP_NAME:
                return self.nodes[i]
        raise DTreeProgrammingError(f"Can't find a root node (with {NodeType.APP_NAME})")

    def get_content(self):
        nodes = []
        for i in range(len(self.nodes)):
            nodes.append(self.nodes[i].get_content())
        return {
            "display_name": self.filename,
            "folder_name": self.dir_name,
            "root_node_id": self.get_root_node().id,
            "node_length": len(self.nodes),
            "nodes": nodes
        }
        
