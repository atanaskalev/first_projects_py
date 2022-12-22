from Errors import *


class Account:
    def __init__(self, balance, currency, acc_type, IBAN):
        self.balance = balance
        self.currency = currency
        self.acc_type = acc_type
        self.IBAN = IBAN

        if balance != float:
            raise InvalidDataFormat
        if currency != "BGN" and currency != "EUR" and currency != "USD" and currency != "JPY":
            raise InvalidAccCurrency
        if acc_type != "CURRENT" and acc_type != "SAVINGS" and acc_type != "CREDIT":
            raise InvalidDataFormat

    def print_1(self):
        return f"Account: {self.balance}, {self.currency}, {self.acc_type}, {self.IBAN}"
