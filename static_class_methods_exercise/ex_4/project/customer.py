class Customer:

    ID = 1
    def __init__(self, name, address, email ):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    @staticmethod
    def get_next_id():
        res = Customer.ID
        Customer.ID += 1
        return res

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"