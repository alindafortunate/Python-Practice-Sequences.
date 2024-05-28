# addinterest.py


def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    balance = newBalance
    print(balance)
    return balance


def test():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print(amount)


test()
