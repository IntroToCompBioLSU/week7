#!/usr/bin/env python
######### Jacobssearight 10.9.2018 Purpose: To take the input of nucelic acid base pairs and output the total number of bases, as well as the number of each particular nucelic acid. 
######### command to run:./Week7Script.sh
######### example user input:AGTC



#Reads the command line input of your DNA sequence and saves it under the variable dnaSeq
dnaSeq = input ("Please input your DNA sequence (capital letters): ")

#Reads the total number of characters within the variable dnaSeq, and prints it to the screen
print ("Total Sequence Length:")
print (len(dnaSeq))

#Reads the number of A (Adenine) within the variable dnaSeq, and prints it to the screen
print ("Number of As:")
print (dnaSeq.count ('A'))

#Reads the number of C (Cytosine) within the variable dnaSeq, and prints it to the screen
print ("Number of Cs:")
print (dnaSeq.count ('C'))

#Reads the number of T (Thymine) within the variable dnaSeq, and prints it to the screen
print ("Number of Ts:")
print (dnaSeq.count ('T'))

#Reads the number of G (Guanine) within the variable dnaSeq, and prints it to the screen
print ("Number of Gs:")
print (dnaSeq.count ('G'))
