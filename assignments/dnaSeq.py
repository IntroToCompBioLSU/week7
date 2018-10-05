#!/usr/bin/env python

userSeq = input("Input DNA sequence: ")

# calculate total sequence lenth
print("Total sequence length")
print(userSeq.count("a") + userSeq.count("g") + userSeq.count("c") + userSeq.count("t"))

# count number of As0
print("Number of As")
print(userSeq.count("a"))

# Count number of Cs
print("Number of Cs")
print(userSeq.count("c"))

# Count number of Gs
print("Number of Gs")
print(userSeq.count("g"))

# Count number of Ts
print("Number of Ts")
print(userSeq.count("t"))




