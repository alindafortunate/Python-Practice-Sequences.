# repeataddinterest1.py
# Repeating the addInterest1.py to understand Functions that Modify Parameters.


def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    balance = newBalance


def test():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print(amount)


test()
# On printing the amount is 1000 because the addInterest() function has no access to the variable amount.
# Note: The formal parameters of a function oly recieve the values of the actual parameters.
