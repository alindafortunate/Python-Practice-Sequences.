# month.py
# A program to print  the abbreviation of a month, given its number.


def main():
    print("This program prints the abbreviations of months of the year\n")
    # month is used as the lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = int(input("Enter a month number (1 - 12): "))

    # Compute starting position of month n in months
    pos = (n - 1) * 3

    # Grab the appropriate slice from months
    monthAbbrev = months[pos : pos + 3]

    # Print the result
    print("The month abbreviation is", monthAbbrev + ".")


main()
