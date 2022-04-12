class Account:
    id = int
    name = str
    Document = str
    Email = str
    password = str

    def __init__(self, name, Document):
        self.name=name
        self.Document = Document
