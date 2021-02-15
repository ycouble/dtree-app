from services.exceptions import DTreeValidationError
from services.xmind_parser.node_type import NodeType

class Node:
    def __init__(self, node_id, title, description={}, style={}, node_type=None):
        self.id = node_id
        self.title = title
        self.description = Node.__format_description(description.get('ops', {}).get('ops', []))
        self.type = node_type if node_type else Node.__set_type(style.get('properties', {}))
        self.href = None
        self.has_links = False
        self.children = []
        self.attachements = []
        if self.type == NodeType.UNDEFINED:
            raise DTreeValidationError(f"Undefined node type !", self)

    def __repr__(self):
        to_print = f"Id: {self.id}\nTitle: {self.title}\nType: {self.type}"
        if len(self.description) != 0:
            to_print += f"\nDescription: {self.description}"
        if self.href != None:
            to_print += f"\nHref: {self.href}"
        to_print += f"\n{len(self.children)} children: {[c.title for c in self.children]}"
        if len(self.attachements) > 0:
            to_print += f"\n{len(self.attachements)} attachements: {[a.title for a in self.attachements]}"
        return to_print

    @staticmethod
    def __set_type(style):
        if style.get('fo:color') == '#ADADAD':
            return NodeType.SKIP
        if not style or not style.get("svg:fill"):
            return NodeType.ANSWER
        node_type = {
            '#E32C2D': NodeType.APP_NAME,
            '#FDD834': NodeType.STEP,
            '#FF6F00': NodeType.STEP,
            '#8EDDF9': NodeType.QUESTION
        }.get(style["svg:fill"], NodeType.UNDEFINED)
        return node_type

    @staticmethod
    def __format_description(description):
        formated = []
        n = 0
        for i in range(len(description)):
            if "attributes" in description[i]:
                formated[n - 1]["attributes"] = description[i]["attributes"].get("list")
                if "insert" in description[i]:
                    formated[n - 1]["insert"] += description[i]["insert"]
            else:
                formated += [description[i]]
                n += 1
        return formated

    def set_href(self, href):
        if type(href) != str:
            raise DTreeValidationError(f"Can't set node href with {type(href)} type", self)
        if "xap:" == href[0:4]:
            self.href = href[4:]
            self.type = NodeType.ATTACHEMENT
        else:
            # TODO: Check link valid ? 
            self.href = href
            self.type = NodeType.EXTERNAL_LINK

    def add_child(self, child_node):
        if self.type in [NodeType.UNDEFINED, NodeType.ATTACHEMENT, NodeType.EXTERNAL_LINK]:
            raise DTreeValidationError(f"Can't add children for {self.type} type", self)
        if child_node.type in [NodeType.UNDEFINED, NodeType.APP_NAME]:
            raise DTreeValidationError(f"Can't add children with {node.type} type", self)
        if child_node.type in [NodeType.ATTACHEMENT, NodeType.EXTERNAL_LINK]:
            self.attachements.append(child_node)
        else:
            self.children.append(child_node)
    
    def get_children_type(self, children=None):
        children_to_test = children if children else self.children
        types = [child.type for child in children_to_test]
        if len(types) == 0:
            return NodeType.UNDEFINED
        if len(set(types)) <= 1:  # Checking type are the same
            return types[0]
        else:
            raise DTreeValidationError(f"Can't have different children type", self)

    def check_errors(self):
        # Children error handling
        children_length = len(self.children)
        children_type = self.get_children_type()
        if self.type in [NodeType.APP_NAME, NodeType.ANSWER, NodeType.SKIP]:
            if children_length != 1:
                raise DTreeValidationError(f"{self.type} node should have only 1 child", self)
            if children_type not in [NodeType.QUESTION, NodeType.STEP, NodeType.SKIP]:
                raise DTreeValidationError(f"{self.type} node can't have {children_type} children type", self)

        if self.type == NodeType.STEP:
            if len(self.description) != 0 and children_length > 1:
                raise DTreeValidationError(f"{self.type} node can't have multiple children and a description", self)
            if len(self.description) == 0 and children_length <= 1:
                raise DTreeValidationError(f"{self.type} node must either have 2 children or a description", self)
            if children_type in [NodeType.QUESTION, NodeType.STEP, NodeType.SKIP] and children_length != 1:
                raise DTreeValidationError(f"{self.type} node can't have multiple {children_type} children", self)
            if children_type == NodeType.ANSWER and children_length < 2:
                raise DTreeValidationError(f"{self.type} node must have multiple {children_type} children", self)
 
        if self.type == NodeType.QUESTION:
            if children_length < 2:
                raise DTreeValidationError(f"{self.type} node must have at least 2 children", self)
            if children_type != NodeType.ANSWER:
                raise DTreeValidationError(f"{self.type} node should have only {NodeType.ANSWER} children", self)
            
    def get_content(self):
        node_content = {
            'id': self.id,
            'title': self.title,
            'type': self.type,
            'children_id': [child.id for child in self.children]
        }
        if len(self.attachements) > 0:
            node_content['attachements_id'] = [doc.id for doc in self.attachements]
        if len(self.description) != 0:
            node_content['description'] = self.description
        if self.href != None:
            node_content['href'] = self.href
        return node_content