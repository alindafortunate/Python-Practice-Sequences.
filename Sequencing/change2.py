# change2.py
# A program to calculate the value of some chnage in dollars
# This version represents the total cash in cents.


def main():

    print("Change counter\n")
    print("Please enter the counter of each coin type.")

    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))

    total = quarters * 25 + dimes * 10 + nickles * 5 + pennies

    print(
        "The total value of your change is ${0}.{1:0>2}".format(
            total // 100, total % 100
        )
    )


main()
