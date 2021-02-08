#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

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
            content += f" -> {[(link.type, link.end_node.node_id) for link in self.links]}"
        print(f"{tabulation}{content}")
        if children_nb != 0:
            for child in self.children:
                child.deep_print(children_nb - 1 if children_nb is not None else None, tab + 1)


