# quadratic3.py
# quadratic2.py
import math


def main():
    print("This program finds the real solution to a quadratic\n")
    a = float(input("Enter the coeffecient a: "))
    b = float(input("Enter the coeffecient b: "))
    c = float(input("Enter the coeffecient c: "))

    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\n The  equation has no real roots.")

    else:
        if discrim == 0:
            root = -b / (2 * a)
            print("\n There is a double root at", root)
        else:
            discRoot = math.sqrt(discrim)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b - discRoot) / (2 * a)
            print("\n The solutions are:", root1, root2)


main()
