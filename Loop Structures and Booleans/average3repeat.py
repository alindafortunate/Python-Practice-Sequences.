# average3repeat.py


def main():
    total = 0.0
    count = 0
    x = float(input("Enter a number (Enter a negative to quit) >> "))

    while x >= 0:
        total = total + x
        count = count + 1
        x = float(input("Enter a number (Enter a negative to quit) >> "))
    print("\n The average of the numbers is: ", total / count)


main()
