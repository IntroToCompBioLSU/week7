#!/usr/bin/env python

#calculate the frequencies of the different bases in a DNA sequences.

dnaSeq = input ("Please enter your DNA sequence: ")

#calculates the length of the entire sequence.
print ("Total Sequence Length:")
print (len(dnaSeq))

#counts number of A's.
print ("Number of As:")
print (dnaSeq.count ('a'))

#counts number of C's.
print ("Number of Cs:")
print (dnaSeq.count ('c'))


#count number of G's.
print ("Number of Gs:")
print (dnaSeq.count ('g'))

#count number of T's.
print ("Number of Ts:")
print (dnaSeq.count ('t'))
