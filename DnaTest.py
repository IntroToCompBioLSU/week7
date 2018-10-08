#!/usr/bin/env python

#calculate the total sentence length

dnaSeq = input ("Please input your DNA sequence: ")

print ("Total Sequence Length:")
print (len(dnaSeq))

print ("Number of As:")
print (dnaSeq.count ('a'))

print ("Number of Cs:")
print (dnaSeq.count ('c'))

print ("Number of Ts:")
print (dnaSeq.count ('t'))

print ("Number of Gs:")
print (dnaSeq.count ('g'))
