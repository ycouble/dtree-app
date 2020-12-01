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

    def deep_print(self, children_nb=None):
        self.root_node.deep_print(children_nb)

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


class Node:
    def __init__(self, title, description, labels, children):
        self.title = title
        self.description = description
        self.labels = labels
        self.children = children

    def __repr__(self):
        return f"Title: {self.title}\nDescription: {repr(self.description)}\nLabels: {self.labels}\nChildren: {child.title for child in self.children}"

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
