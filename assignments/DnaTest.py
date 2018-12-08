#!/usr/bin/env python

#calculate the total sentence length

dnaSeq = input ("Please input your DNA sequence: ")

print ("Total Sequence Length:")
print (len(dnaSeq))

print ("Number of As:")
print (dnaSeq.lower().count ('a'))

print ("Number of Cs:")
print (dnaSeq.lower().count ('c'))

print ("Number of Ts:")
print (dnaSeq.lower().count ('t'))

print ("Number of Gs:")
print (dnaSeq.lower().count ('g'))

# DB: Good, although it doesn't count properly if you give it an uppercase sequence.
#     Adding .lower() to the sequence will fix this.