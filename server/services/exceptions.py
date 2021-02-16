
class DTreeValidationError(Exception):
    def __init__(self, message, node=None):

        super().__init__(f"{message}\n\n{node}")

        self.node = node

class DTreeProgrammingError(Exception):
    pass

class FileUploadError(Exception):
    pass

class PyMongoError(Exception):
    pass