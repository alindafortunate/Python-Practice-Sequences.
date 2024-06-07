# average3repeat.py

# This program causes a division error when you enter a 0 at the start so it's not the best.


def main():
    total = 0.0
    count = 0
    x = float(input("Enter a number ('Enter 0 to stop') >> "))

    while x != 0:

        total = total + x
        count = count + 1
        x = float(input("Enter a number (Enter stop to quit) >> "))

    print("\n The average of the numbers is: ", total / count)


main()
