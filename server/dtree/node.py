#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
from dtree.link import LinkType

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
        self.type = self.set_type(style.get('properties')) if style else NodeType.TEXT
        self.links = []
        # if node_id == "7c4d8d46-be35-4e79-ba91-1d27830a791a":
        #     import pdb; pdb.set_trace()

    def __repr__(self):
        return f"Id: {self.node_id}\nText: {self.text}\nChildren: {child.text for child in self.children}"

    def set_type(self, style):
        if style.get('fo:color') == '#ADADAD':
            return NodeType.SKIP
        if not style or not style.get("svg:fill"):
            return NodeType.TEXT
        node_type = {
            '#FDD834': NodeType.TITLE,
            '#8EDDF9': NodeType.QUESTION,
            '#FF6F00': NodeType.QUESTION # SKIP ? 
        }.get(style["svg:fill"], NodeType.TEXT)
        if self.text == "(*) ETAPE 4 : GESTION DES LOTS SUSPECTS": #TODO : Change color on xmind.
            node_type = NodeType.TITLE
        # if node_type == NodeType.SKIPand style.get('fo:color') != '#ADADAD':
        #     node_type = NodeType.TEXT 
        return node_type

    def get_children_type(self):
        types = [child.type for child in self.children]
        if len(set(types)) <= 1: # Checking type are the same
            return types[0]
        else:
            return None #TODO : Error management

    def get_links_type(self):
        types = [link.type for link in self.links]
        if len(set(types)) <= 1: # Checking type are the same
            return self.links[0].type
        else:
            return None #TODO : Error management

    def get_next_node(self):
        if len(self.children) == 1:
            if self.children[0].type == NodeType.SKIP:
                return self.children[0].get_next_node()
            else:
                return self.children[0].node_id
        return None #TODO : Error management

    def get_content(self):
        if len(self.children) == 1:
            return {
                'id': self.node_id,
                'text': self.text,
                'next_node_id': self.get_next_node()
            }
        return None #TODO : Error management

    def get_following_choice(self):
        if len(self.links) == 0: # If links ignore children node
            if len(self.children) > 1 or self.get_children_type() == NodeType.TEXT:
                return [child.get_content() for child in self.children]
            elif len(self.children) == 1:
                return self.children[0].get_following_choice()
        else:
            if self.get_links_type() == LinkType.CHOICE:
                return [link.get_content() for link in self.links]
            elif len(self.links) == 1 and self.get_links_type() == LinkType.REDIRECT:
                return [self.links[0].end_node.get_content()]
        return None #TODO: Error management (can be end)

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


