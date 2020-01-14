class Schema:
    def __init__(self, name, *fields):
        self.fields = fields


class Field:
    def __init__(self, name, dtype):
        self.name = name
        self.type = dtype
