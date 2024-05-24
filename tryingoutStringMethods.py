# tryingoutStringMethods.py
# Trying out more string methods.


def main():
    s = "hello, the Lord will save you!"

    # Capitalises the first letter of the first word.
    print(s.capitalize())
    # Capitalises the first letter of every word.
    print(s.title())
    # Changes everything to lower case
    print(s.lower())
    # Changes everything to uppercase.
    print(s.upper())
    # Replaces the word with another
    print(s.replace("the Lord", "Jesus Christ"))
    # Centers the string
    print(s.center(30))
    print(s.center(50))
    # Counts the similar letters in a string
    print(s.count("e"))
    # Finds the position of the number
    print(s.find(","))
    # Joins a list into a string
    print(" ".join(["Number", "one,", "the", "Lord"]))


main()
