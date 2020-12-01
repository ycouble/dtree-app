#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from zipfile import ZipFile


XMIND_FILE = "test.xmind"


class DTree:
    def __init__(self, filename=XMIND_FILE):
        self.filename = filename
        self.raw_json_data = DTree._extract_zip(self.filename)
        self.root_node = DTree._populate_node(self.raw_json_data[0]["rootTopic"])

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
        description = data["notes"]["plain"]["content"] if "notes" in data else None
        children = []
        if "children" in data:
            children = [DTree._populate_node(child) for child in data["children"]["attached"]]
        return Node(data.get("title"), description, data.get("labels"), children)

    def get_node(self, node_id, node=None):
        if node == None:
            node = self.root_node
        print(node_id, node.get_id())
        if node_id == node.get_id():
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

class Node:
    def __init__(self, title, description, labels, children):
        self.title = title
        self.description = description
        self.labels = labels
        self.children = children

    def __repr__(self):
        return f"Title: {self.title}\nDescription: {repr(self.description)}\nLabels: {self.labels}\nChildren: {child.title for child in self.children}"

    def get_id(self):
        return id(self)

    def get_content(self):
        return {
            'id': self.get_id(),
            'question': self.title,
            'description': self.description,
            'choices': [
                {'labels': child.labels, 'id': child.get_id()} for child in self.children
            ]
        }

    def deep_print(self, children_nb=None, tab=0):
        tabulation = "|    " * (tab - 1)
        if tab != 0:
            tabulation += "|---"
        content = f"{self.labels} -> {self.title} - {repr(self.description)}"
        print(f"{tabulation}{content}")
        if children_nb != 0:
            for child in self.children:
                child.deep_print(children_nb - 1 if children_nb is not None else None, tab + 1)



if __name__ == "__main__":
    dtree = DTree()
    dtree.deep_print()
