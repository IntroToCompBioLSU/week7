#!/usr/bin/env python

#For the different bases in the DNA sequences calculate the frequencies.

dnaSeq = input ("Enter your DNA sequence:")

#Begin calculating the entire length of the given sequence.
print ("Total Sequence Length:")
print (len(dnaSeq))

#count total number of A's.
print ("Number of As:")
print (dnaSeq.count ('a'))

#count total number of C's.
print ("Number of Cs:")
print (dnaSeq.count ('c'))

#count total number of G's.
print ("Number of Gs:")
print (dnaSeq.count ('g'))

#count total number of T's.
print ("Number of Ts:")
print (dnaSeq.count ('t'))
