import json

from enum import Enum

class NodeType(Enum):
    UNDEFINED = 0
    APP_NAME = 1
    STEP = 2
    QUESTION = 3
    ANSWER = 4
    ATTACHEMENT = 5
    EXTERNAL_LINK = 6
    SKIP = 7

# json.dumps(data, cls=EnumEncoder)
# json.loads(text, object_hook=as_enum)

class NodeTypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj) == NodeType:
            _, member = str(obj).split(".")
            return member
        return json.JSONEncoder.default(self, obj)

def as_enum(d):
    if "type" in d:
        return getattr(NodeType, d["type"])
    else:
        return d