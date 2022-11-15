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

ACCOUNTS = [10, 100, 20, 50, 30]

class Input:
    def __init__(self, ammount):
        self.ammount = ammount
    def __str__(self):
        return self.ammount

class Funds:
    def __init__(self):
        self.accounts = [10, 100, 20, 50, 30]
    def __str__(self):
        return self.accounts

    def add_income(self, ammount):
        income = Input(ammount)
        account = self.accounts
        my_account = int(to_account_number)
        sum = account[my_account] + ammount
        account.pop(my_account)
        account.insert(my_account, sum)

    def 


funds = Funds()

while True:
    print("Enter your request: ")
    print("1 - transfer")
    print("2 - deposit")
    print("3 - withdraw")

    choice = input()

    if choice == "1":
        print("Enter amount: ")
        ammount = int(input("Amount: "))
        # print("From which account you want to transfer:")
        # from_account_number = input("Choose account 1 2 3 4 5: ")
        print("To what account you want to transfer your funds:")
        to_account_number = input("Choose account 1 2 3 4 5: ")

        funds.add_income(ammount)
        print("Pajamos įvestos sėkmingai!")
        print(funds.accounts)

