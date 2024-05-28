# happy.py
# A program to print the lyrics of a happy birthday song.
# defining functions


def happy():
    print("Happy Birthday to you!")


def singFred():
    happy()
    happy()
    print("Happy Birthday to you, dear Fred")
    happy()


def singLucy():
    happy()
    happy()
    print("Happy Birthday, dear Lucy")
    happy()


# Lets write a generic function called to avoid duplication
def sing(person):
    happy()
    happy()
    print("Happy Birthday dear", person + ".")
    happy()


def main():
    singFred()
    print()
    singLucy()

    print()
    print()
    sing("Fortunate")
    print()
    sing("Lucky")


main()
