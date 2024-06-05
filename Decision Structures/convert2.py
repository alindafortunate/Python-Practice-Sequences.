# convert2.py
# A program to convert Celsius temps to Fahrenheit
# This version issues  heat and cold warnings.


def main():
    celcius = float(input("What is the temperature? "))
    fahrenheit = 9 / 5 * celcius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    # Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful! ")

    if fahrenheit < 30:
        print("Brrrr. Be sure to dress warmly! ")


main()
