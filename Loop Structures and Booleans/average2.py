# average2.py


def main():
    n = int(input("How many numbers are there? "))
    total = 0.0
    for i in range(n):
        x = float(input("Enter the number >>: "))
        total = total + x
    print("\n The average of the numbers is: ", total / n)


main()
