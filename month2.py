# month2.py
# Now using lits


def main():
    # Months is a list used a lookup table
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    n = int(input("Enter a month number(1 - 12): "))
    print("The month abbreviation is", months[n - 1] + ".")

    # Months with full names
    monthsWithFullNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    n = int(input("Enter a month number(1 - 12): "))
    print("The month abbreviation is", monthsWithFullNames[n - 1] + ".")


main()
