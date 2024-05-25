# fileprocessing.py
# Understanding file processing.
# A file is a sequence of data that is stored in secondary memory (usually on a disk drive).

"""Note I have actually realised that, saying def main(): it means that
you are creating a new function called main and you should invoke it with main() at the end.

in simple terms it can even be

def newFunction()

    #Python statements.
    #Python statements.
    #Python statements.

newFunction()
"""
# While working with text files in Python,
# the first step is to create a file object corresponding to a file on disk,
# this is done using the open function.

# Usually a file object is assigned to a variable like this
# <variable> = open(<name> , <mode>)

# The mode is usually "r" for reading from the file and "w" for writing to the file.


# Example
def main():

    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)

    # Second file processing example.
    infile2 = open("tryingoutStringMethods.py", "r")
    for i in range(5):
        line = infile2.readline()
        print(line[:-1])


main()
