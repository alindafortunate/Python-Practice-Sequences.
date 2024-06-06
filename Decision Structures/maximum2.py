# maximum2.py
# Applying the decision tree


def main():
    print("This program prints the maximum number entered by the user.")

    x1 = input("Enter the first value: ")
    x2 = input("Enter the second value: ")
    x3 = input("Enter the third value: ")

    # Checking the maximum value
    if x1 >= x2:
        if x1 >= x3:
            print("The maximum value is: ", x1)
        else:
            print("The maximum value is: ", x3)
    else:
        if x2 >= x3:
            print("The maximum value is: ", x2)
        else:
            print("The maximum value is: ", x3)


main()
