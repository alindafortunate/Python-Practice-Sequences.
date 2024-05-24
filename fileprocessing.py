# fileprocessing.py
# Understanding file processing.
# A file is a sequence of data that is stored in secondary memory (usually on a disk drive).


# Example
def main():

    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)


main()
