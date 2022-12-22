from entities import Errors
from entities import Bank
from entities import Account
from entities import User

class Menu:
    def print_menu(self):
        print("1.Create user")
        print("2.Create account for user")
        print("3.List users")
        print("4.List account for user")
        print("5.Deposit for user account")
        print("6.Withdrawal for user account")
        print("7.Exit")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Choose an item from the menu")

            if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and \
                    choice != "6" and choice != "7":
                break

    def CreateUser(self):
        egn = input("Enter EGN")
        name = input("Enter Name")
        user = User(egn, name)

