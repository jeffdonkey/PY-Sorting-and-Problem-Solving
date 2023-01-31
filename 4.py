# Write an algorithm that takes in a string and sorts the words
#  in the string in alphabetical order.
#  The comparison should be case-insensitive.

    # Sample input: 'I love software engineering'
    # Sample output: ['engineering', 'I', 'love', 'software']
    # Note that a key parameter will need to be used here in order
    #  for the sorting to be case-insensitive
    #  (sort in alphabetical order regardless of whether string
    #  is uppercase or lowercase).

myString = "I love software engineering"

newString = sorted(myString.split(), key=str.lower)

print(newString)

    # on line 14 'split()' is a function used to split
    # a string.  The default is any whitespace.