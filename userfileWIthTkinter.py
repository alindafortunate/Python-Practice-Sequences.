# userfile.py
# Program to create a file of usernames in batch mode

# Including dialog box from tkinter to
# help users easily locate files with a dialog box.

from tkinter.filedialog import askopenfilename, asksaveasfilename


def main():

    print("This program creates  a file of usernames from a")
    print("file of names.")

    # get the file names.
    infileName = askopenfilename()
    outfileName = asksaveasfilename()

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
