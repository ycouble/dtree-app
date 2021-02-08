#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from zipfile import ZipFile

from node import Node
from link import Link, LinkType

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
        return Node(data.get("id"), data.get("title", " "), children, data.get("style"))

    def create_relationships(self, relationships):
        for relation in relationships:
            start_node = self.get_node(relation['end1Id'])
            end_node = self.get_node(relation['end2Id'])
            link = Link(relation['id'], relation.get('title', ""), start_node, end_node)
            if not start_node or not end_node:
                import pdb;pdb.set_trace() #TODO error management
                print(relation['end1Id'], relation['end2Id'])
            start_node.links.append(link)
            links = (link for link in start_node.links if len(start_node.links) > 1)
            for choice_link in links:
                choice_link.type = LinkType.CHOICE


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

if __name__ == "__main__":
    dtree = DTree()
    dtree.deep_print()
    import pdb; pdb.set_trace()
