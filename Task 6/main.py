# Sukurkite terminalo programą, kuri bankui leis apdoroti gaunamas užklausas. Bankas gali gauti trijų tipų užklausas:

# - transfer i j sum: prašymas pervesti pinigų sumą iš i-osios sąskaitos į j-ąją;
# - deposit i sum: prašymas įnešti pinigų sumą į i-ąją sąskaitą;
# - withdraw i sum: prašymas išsiimti pinigų sumą iš i-osios sąskaitos.

# Jūsų programa taip pat turėtų galėti apdoroti netinkamas užklausas. Yra dviejų tipų negaliojančios užklausos:
# - neteisingas sąskaitos numeris prašymuose;
# - didesnės pinigų sumos, nei yra šiuo metu, išėmimas/pervedimas.

# Po kiekvienos operacijos išveskite ar ji pavyko, ar ne ir parodykite sąskaitų balansus ekrane.

######################

# Pvz. Kai duoti pradiniai sąskaitų balansai yra:
# ACCOUNTS = [10, 100, 20, 50, 30]

# Įvestos užklausos į terminalą:
# - "withdraw 2 10"
# - "transfer 5 1 20"
# - "deposit 5 20"
# - "transfer 3 4 15"

# Atitinkamai išvedami rezultatai, po kiekvienos užklausos:
# - Operation was successful; New account balances: [10, 90, 20, 50, 30]
# - Operation was successful; New account balances: [30, 90, 20, 50, 10]
# - Operation was successful; New account balances: [30, 90, 20, 50, 30]
# - Operation was successful; New account balances: [10, 90, 20, 50, 30]
# - Operation was successful; New account balances: [30, 90, 5, 65, 30]

######################

# Pvz. Kai duoti pradiniai sąskaitų balansai yra:
# ACCOUNTS = [20, 1000, 500, 40, 90]

# Įvestos užklausos į terminalą:
# - "deposit 3 400"
# - "transfer 1 10 10"
# - "withdraw 4 50"

# Atitinkamai išvedami rezultatai, po kiekvienos užklausos:
# - Operation was successful; New account balances: [20, 1000, 900, 40, 90]
# - Operation is invalid, such account does not exist; New account balances: [20, 1000, 900, 40, 90]
# - Operation is invalid, not enough balance; New account balances: [20, 1000, 900, 40, 90]

# !!! Pastaba: Papildomas taškas, jeigu panaudosite klases. !!!
# ACCOUNTS = [10, 100, 20, 50, 30]

class Operations:
    def __init__(self, name):
        self.name = name

class Check_operations():

    def fund_check(ammount):
        accounts = funds.accounts
        account_to_check = int(from_account_number)
        if accounts[account_to_check] < ammount:
            print("")
            print("!!Not enough funds in your account!!")
            return True

    def ammount_check(ammount):
        if ammount <= 0:
            print("")
            print("!!!Ammount must be above zero!!!")
            return True

    def account_number_check_1(ammount):
        if int(from_account_number) > 5 or int(from_account_number) <= 0:
            print("")
            print("!!!Wrong account number!!!")
            return True

    def account_number_check_2(ammount):
        if int(to_account_number) > 5 or int(to_account_number) <= 0:
            print("")
            print("!!!Wrong account number!!!")
            return True


class Funds_operations():
    def __init__(self):
        self.accounts = ["", 10, 100, 20, 50, 30]

    def withdraw_funds(self, ammount):
        account = self.accounts
        my_account = int(from_account_number)
        difference = account[my_account] - ammount
        account.pop(my_account)
        account.insert(my_account, difference)

    def add_funds(self, ammount):
        account = self.accounts
        to_account = int(to_account_number)
        sum = account[to_account] + ammount
        account.pop(to_account)
        account.insert(to_account, sum)

funds = Funds_operations()

class print_Operations(Operations):
    def __init__(self, name):
        super().__init__(name)

    def print_1(self):
        print("Enter", self.name, "amount: ")

    def print_2(self):
        print("Enter account you want to", self.name, "FROM?:")

    def print_3(self):
        print("Enter account you want to", self.name, "TO?:")

    def print_4(self):
        print("")
        print(self.name, "succesfull!!!")


while True:
    print("")
    print("Your balance: ", [i for i in funds.accounts if i or i == 0])
    print("Enter operation number: ")
    print("1 - transfer")
    print("2 - deposit")
    print("3 - withdraw")

    choice = input()

    if choice == "1":
        choice_1 = Operations("transfer")
        print_Operations.print_1(choice_1)
        ammount = int(input("Amount: "))
        if Check_operations.ammount_check(ammount):
            pass
        else:
            print_Operations.print_2(choice_1)
            from_account_number = input("Choose account 1 2 3 4 5 : ")
            if Check_operations.account_number_check_1(from_account_number):
                pass
            elif Check_operations.fund_check(ammount):
                pass
            else:
                print_Operations.print_3(choice_1)
                to_account_number = input("Choose account 1 2 3 4 5 : ")
                if Check_operations.account_number_check_2(to_account_number):
                    pass
                else:
                    funds.withdraw_funds(ammount)
                    funds.add_funds(ammount)
                    print_Operations.print_4(choice_1)

    if choice == "2":
        choice_2 = Operations("deposit")
        print_Operations.print_1(choice_2)
        ammount = int(input("Amount: "))
        if Check_operations.ammount_check(ammount):
            pass
        else:
            print_Operations.print_3(choice_2)
            to_account_number = input("Choose account 1 2 3 4 5 : ")
            if Check_operations.account_number_check_2(to_account_number):
                pass
            else:
                funds.add_funds(ammount)
                print_Operations.print_4(choice_2)

    if choice == "3":
        choice_3 = Operations("withdraw")
        print_Operations.print_1(choice_3)
        ammount = int(input("Amount: "))
        if Check_operations.ammount_check(ammount):
            pass
        else:
            print_Operations.print_2(choice_3)
            from_account_number = input("Choose account 1 2 3 4 5 : ")
            if Check_operations.account_number_check_1(from_account_number):
                pass
            elif Check_operations.fund_check(ammount):
                pass
            else:
                funds.withdraw_funds(ammount)
                print_Operations.print_4(choice_3)
