class InvalidCommand(Exception):
    def __init__(self):
        print("Invalid command")


class InvalidDataFormat(Exception):
    def __init__(self):
        print("Invalid data format")


class InvalidAccCurrency(Exception):
    def __init__(self):
        print("Invalid account currency")


class InvalidAccountType(Exception):
    def __init__(self):
        print("Invalid account type")


class UserNotFound(Exception):
    def __init__(self):
        print("User not found")


class AccNotFound(Exception):
    def __init__(self):
        print("Account not found")
