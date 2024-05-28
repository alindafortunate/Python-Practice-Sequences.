# Functions with values
# A program that has functions returning values.
def square(x):
    return x**2


def main():
    print("The square of the actual parameter of x is: ", square(2))

    x = 7
    y = square(x)

    print("The value of y is: ", y)


main()
