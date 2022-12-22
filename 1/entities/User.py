from Errors import *


class User:
    def __init__(self, accounts, names, EGN):
        self.accounts = accounts
        self. names = names
        self.EGN = EGN

        if len(accounts) < 4:
            raise InvalidDataFormat
        if len(EGN) != 10 and EGN != int:
            raise InvalidDataFormat

    def print_1(self):
        return f"User: {self.accounts}, {self.names}, {self.EGN}"
