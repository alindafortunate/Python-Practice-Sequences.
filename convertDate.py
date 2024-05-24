# convertMonth.py
# A program that converts a date in the form 'mm/dd/yyyy' to "month day, year"".


def main():

    # Get date
    dateStr = input("Enter a date (mm/dd/yyyy): ")
    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert month string to month name
    months = [
        "January",
        "Febbruary",
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
    monthStr = months[int(monthStr) - 1]

    # Output results in month day, year format.
    print("The converted date is:", monthStr, dayStr + ",", yearStr)


main()
