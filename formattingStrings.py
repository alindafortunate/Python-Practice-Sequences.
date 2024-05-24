# formattingStrings.py
# How formatting of strings works.
print("Hello {0} {1}, you may have won ${2}".format("Mr.", "Smith", 10000))

# Formating applying the width.
print("This int, {0:5}, was placed in a field of width 5".format(7))
print("This int, {0:10}, was placed in a field of width 10".format(7))

# Formating applying width and precision.
print("This float, {0:10.5}, has width 10 and precision 5".format(3.1415926))

# Formating applying decimal places.
print("This float, {0:10.5f}, is fixed at 5 decimal places".format(3.1415926))

# Working with width and precision.
print("This float, {0:0.5}, has width 0 and precision 5".format(3.1415926))

print("Compare {0} and {0:0.20}".format(3.14))

# Aligning content to the left, right and center using < , > and
print("left justification: {0:<5}".format("Hi!"))

print("right justification: {0:>5}".format("Hi!"))
