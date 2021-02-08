#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

class LinkType(Enum):
    CHOICE = 5
    REDIRECT = 6

class Link:
    def __init__(self, link_id, text, start_node, end_node):
        self.link_id = link_id
        self.text = text
        self.start_node = start_node
        self.end_node = end_node
        self.type = LinkType.REDIRECT

    def __repr__(self):
        return f"Id: {self.link_id}\nText: {self.text}\nFrom: {self.start_node.text}\To: {self.end_node.text}"
