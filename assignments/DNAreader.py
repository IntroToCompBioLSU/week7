#!/usr/bin/env python

DNASeq = input("Enter DNA Sequence to be Analized: ")
#convert to upper
DNASeq = DNASeq.upper()

print ("DNA Sqecuence to be Analized: ")
print (DNASeq)
print (" ")
print ("Sequence Length: ", end =" ")
print (len(DNASeq))
print (" ")
#Number of A's:
print ("Count of A's: ", end = " ")
print (DNASeq.count("A"))
#Number of C's:
print ("Count of C's: ", end = " ")
print (DNASeq.count("C"))
#Number of G's:
print ("Count of G's: ", end = " ")
print (DNASeq.count ("G"))
#Number of T's:
print ("Count of T's: ", end = " ")
print (DNASeq.count ("T"))

# DB: Good! Nicely done.