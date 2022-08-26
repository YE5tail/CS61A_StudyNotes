# attributes extended

class Account:
    interest = 0.04

    def __init__(self, holder):
        self.holder = holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        self.balance -= amount
        return self.balance

>>> noah_account = Account('Noah')
>>> noah_account.interest = 0.05
# instance attribute assignment, the name 'interest' is not looked up,
# attribut assignment statement adds or modifies the attribute named 'interest'
# to noah_account 即在noah_account条目下会多一条名为‘interest’的attribute

# inheritance

# sub-class (or specialised class) has most attributes same to the general class,
# except for, or along with, some special-case behavior.

# a checking account is a specialised Account
# which has a lower interest rate and incur a withdraw fee

class CheckingAccount(Account): # base class is Account
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)


>>> noah_ch = CheckingAccount('Noah') # calls Account.__init__
>>> noah_ch.interest # found in CheckingAccount
0.01
>>> noah_ch.deposit(20) # found in Account
20
>>> noah_ch.withdraw(5) # found in CheckingAccount
14

class Bank:
    """A bank *has* Accounts"""
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        """create an account of specific kind"""
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self) > 1

>>> bear_bank = Bank() # create a bank
>>> noah = bear_bank.open_account('Noah', 20)
>>> sandra = bear_bank.open_account('Sandra', 10, CheckingAccount)
>>> noah.interest
0.04
>>> sandra.interest
0.01
>>> bear_bank.pay_interest() # a method needs to use ()
>>> noah.balance
20.8
>>> sandra.balance
10.1

class SavingAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)

# multiple inheritance

class CleverAccount(CheckingAccount, SavingAccount):
    """
    low interest of 4%
    a $2 fee for deposits
    a $1 fee for withdrawls
    a free $1 upon opening account
    """
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1 # a free $1

>>> such_a_deal = CleverAccount('John')
>>> such_a_deal.balance
1
>>> such_a_deal.deposit(100)
99
>>> such_a_deal.withdraw(20)
78
