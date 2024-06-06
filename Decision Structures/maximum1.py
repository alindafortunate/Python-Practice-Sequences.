# maximum1.py
def main():
    print("A program that prints the maximum number that the user enter\n")
    x1, x2, x3 = input("Enter three number e.g 1, 2,3: ")
    if x1 > x2 > x3:
        print("The maximum number is ", x1)
    elif x2 > x3 > x1:
        print("The maximum number is ", x2)
    elif x3 > x2 > x1:
        print("The maximum number is ", x3)
    elif x1 > x3 > x2:
        print("The value is ", x1)
    elif x1 > x2 < x3:
        print("The value is ", x3)
    else:
        print("The maximum value is ", x2)


main()
