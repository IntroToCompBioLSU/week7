#!/usr/bin/env python

#Provide a DNA Sequence
DNASeq = input("Insert DNA Sequence: ")

#Count the entire DNA Sequence
print ("Entire DNA Sequence Base Length")
print (len(DNASeq))

#Count the number of A's in the sequence
print ("Number of A's")
print (DNASeq.count ('A') + (DNASeq.count ('a')))

#Count the number of T's in the sequence
print ("Number of T's")
print (DNASeq.count ('T') + (DNASeq.count ('t')))

#Count the number of C's in the sequence
print ("Number of C's")
print (DNASeq.count ('C') + (DNASeq.count ('c')))

#Count the number of G's in the sequence
print ("Number of G's")
print (DNASeq.count ('G') + (DNASeq.count ('g')))

# DB: Good! You could also avoid separately counting upper and lower cases
#     by converting the sequence to one or the other using .upper() or .lower().