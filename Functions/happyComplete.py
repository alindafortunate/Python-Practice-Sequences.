# happyComplete.py
# A complete program for happy.py printing for atleast four people.


def happy():
    print("Happy Birthday to you!")


def sing(person):
    happy()
    happy()
    print("Happy Birthday dear", person + ".")
    happy()


def main():
    sing("Brendah")
    print()
    sing("Fortunate")
    print()
    sing("Lucky")
    print()
    sing("Jonan")


main()
