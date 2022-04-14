from account import Account

class User(Account):
    id=int

    def __init__(self, name, Document):
        super().__init__(name, Document) 
