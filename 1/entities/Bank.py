class Bank:
    def __init__(self, users, add_user):
        self.users = users
        self.add_user = add_user

    def print_1(self):
        return f"Bank: {self.users}"
