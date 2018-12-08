#! /usr/bin/python
#program expects a DNA Sequence of letters
#will work as a word count function for every letter in a string
def count_dict(mystring):
    count = {}
# count
    for word in mystring: 
        count[word] = mystring.count(word)
# prints in order a-c-g-t
    for letter in sorted(count):
        print (letter + ': ' + str(count[letter]))
mystring = input("Enter Your DNA Sequence: ")
count_dict(mystring)

# DB: Good! The only thing I had trouble with is that the input sequence has to be
#     quoted, which I didn't realize at first. Not that important for such a simple
#     script, but it's a good idea to document the purpose of each section of code.