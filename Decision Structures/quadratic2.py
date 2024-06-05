# quadratic2.py
import math


def main():
    print("This program finds the real solution to a quadratic\n")
    a = float(input("Enter the coeffecient a: "))
    b = float(input("Enter the coeffecient b: "))
    c = float(input("Enter the coeffecient c: "))

    discrim = b * b - 4 * a * c
    if discrim >= 0:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\n The solutions are:", root1, root2)
    else:
        print("\n The  equation has no real roots.")


main()
