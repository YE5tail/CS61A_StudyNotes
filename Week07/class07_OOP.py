# objece_oriented programming (OOP)

# the class statement
class Account:
    """An account has its balance and its holder's name"""

    interest = 0.02 # a class attributes, shared across all instances

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    # additional methods are defined as bellow

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        self.balance -= amount
        return self.balance

a = Account('Noah')
a.balance

# binding an object to a new name using assignment does not create a new object
c = a
c is a "True"

a.deposit(540)
a.withdraw(200)

# attributes built-in functions
getattr(a, 'balance')
hasattr(a, 'balance')

# function and method
type(Account.deposit) "function"
type(a.deposit) "method"
Account.deposit(a, 1000) # using function
