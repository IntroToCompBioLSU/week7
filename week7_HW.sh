#!/usr/bin/env python

#calculate the frequencies of the different bases in a DNA sequences.

dnaSeq = input ("Please enter your DNA sequence: ")

#calculates the length of the entire sequence.
print ("Total Sequence Length:")
print (len(dnaSeq))

#counts number of A's.
print ("Number of As:")
print (dnaSeq.lower().count ('a'))

#counts number of C's.
print ("Number of Cs:")
print (dnaSeq.lower().count ('c'))


#count number of G's.
print ("Number of Gs:")
print (dnaSeq.lower().count ('g'))

#count number of T's.
print ("Number of Ts:")
print (dnaSeq.lower().count ('t'))

# DB: Good! The only potential problem is that the script breaks if the
#     sequence is uppercase. Adding .lower() to dnaSeq (see above) would
#     fix this.