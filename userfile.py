# userfile.py
# Program to create a file of usernames in batch mode


def main():

    print("This program creates  a file of usernames from a")
    print("file of names.")

    # get the file names.
    infileName = input("What files are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # Open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # Process each line of the input file
    for line in infile:
        # get the first and last names from the line.
        first, last = line.split()

        # Create the username.
        uname = (first[0] + last[:7]).lower()

        # Write it to the output file.
        print(uname, file=outfile)

    # Close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)


main()
