#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from zipfile import ZipFile
from enum import Enum


XMIND_FILE = "salmonelles.xmind"


class DTree:
    def __init__(self, filename=XMIND_FILE):
        self.filename = filename
        self.raw_json_data = DTree._extract_zip(self.filename)
        self.root_node = DTree._populate_node(self.raw_json_data[0]["rootTopic"])
        if "relationships" in self.raw_json_data[0]:
            self.create_relationships(self.raw_json_data[0]["relationships"])

    def __repr__(self):
        return f"DTree from {self.filename}"

    @staticmethod
    def _extract_zip(input_zip):
        # TODO: Error managment, wrong file
        input_zip = ZipFile(input_zip)
        json_bytes = input_zip.read("content.json") 
        json_data = json.loads(json_bytes.decode('utf-8'))
        return json_data

    @staticmethod
    def _populate_node(data):
        # TODO: Error managment
        children = []
        if "children" in data:
            children = [DTree._populate_node(child) for child in data["children"]["attached"]]
            if "summary" in data["children"]:
                valid_children = (child for child in children if len(child.children) == 0)
                summaries = [DTree._populate_node(summary) for summary in data["children"]["summary"]]
                for child in valid_children:
                    child.children = summaries
        return Node(data.get("id"), data.get("title"), children, data.get("style"))

    def create_relationships(self, relationships):
        for relation in relationships:
            start_node = self.get_node(relation['end1Id'])
            end_node = self.get_node(relation['end2Id'])
            link = Link(relation['id'], relation.get('title', ""), start_node, end_node)
            if not start_node or not end_node:
                import pdb;pdb.set_trace() #TODO error management
                print(relation['end1Id'], relation['end2Id'])
            start_node.links.append(link)

    def get_node(self, node_id, node=None):
        if node == None:
            node = self.root_node
        if node_id == node.node_id:
            return node
        for child in node.children:
            result = self.get_node(node_id, child)
            if result is not None:
                return result
        return None

    def print_raw_json(self):
        print(json.dumps(self.raw_json_data, sort_keys=True, indent=4, ensure_ascii=False))

    def deep_print(self, children_nb=None):
        self.root_node.deep_print(children_nb)

class NodeType(Enum):
    TITLE = 1
    TEXT = 2
    QUESTION = 3
    SKIP = 4

class Node:
    def __init__(self, node_id, text, children, style):
        self.node_id = node_id
        self.text = text
        self.children = children
        self.type = self.get_type(style.get('properties')) if style else NodeType.TEXT
        self.links = []
        # if node_id == "7c4d8d46-be35-4e79-ba91-1d27830a791a":
        #     import pdb; pdb.set_trace()

    def __repr__(self):
        return f"Id: {self.node_id}\nText: {self.text}\nChildren: {child.text for child in self.children}"

    def get_type(self, style):
        if style.get('fo:color') == '#ADADAD':
            return NodeType.SKIP
        if not style or not style.get("svg:fill"):
            return NodeType.TEXT
        node_type = {
            '#FDD834': NodeType.TITLE,
            '#8EDDF9': NodeType.QUESTION,
            '#FF6F00': NodeType.SKIP
        }.get(style["svg:fill"], NodeType.TEXT)
        if self.text == "(*) ETAPE 4 : GESTION DES LOTS SUSPECTS": #TODO : Change color on xmind.
            node_type = NodeType.TITLE
        # if node_type == NodeType.SKIPand style.get('fo:color') != '#ADADAD':
        #     node_type = NodeType.TEXT 
        return node_type

    def get_content(self):
        return {
            'id': self.node_id,
            'text': self.text,
            'choices': [
                {'text': child.text, 'id': child.node_id} for child in self.children
            ],
            'links': [
                {'text': link.text, 'id': link.link_id, 'dest_id': link.end_node.id} for link in self.links
            ]
        }

    def deep_print(self, children_nb=None, tab=0):
        tabulation = "|    " * (tab - 1)
        if tab != 0:
            tabulation += "|---"
        content = f"{self.type}: {self.text[0:30]}"
        # content = f"{content} - {self.node_id}"
        if self.links:
            content += f" -> {[link.end_node.node_id  for link in self.links]}"
        print(f"{tabulation}{content}")
        if children_nb != 0:
            for child in self.children:
                child.deep_print(children_nb - 1 if children_nb is not None else None, tab + 1)

class Link:
    def __init__(self, link_id, text, start_node, end_node):
        self.link_id = link_id
        self.text = text
        self.start_node = start_node
        self.end_node = end_node

    def __repr__(self):
        return f"Id: {self.link_id}\nText: {self.text}\nFrom: {self.start_node.text}\To: {self.end_node.text}"


if __name__ == "__main__":
    dtree = DTree()
    dtree.deep_print()
    import pdb; pdb.set_trace()
