#!/usr/bin/env python

userSeq = input("Input DNA sequence: ")

# calculate total sequence lenth
print("Total sequence length")
print(userSeq.count("a") + userSeq.count("g") + userSeq.count("c") + userSeq.count("t"))

# count number of As0
print("Number of As")
print(userSeq.lower().count("a"))

# Count number of Cs
print("Number of Cs")
print(userSeq.lower().count("c"))

# Count number of Gs
print("Number of Gs")
print(userSeq.lower().count("g"))

# Count number of Ts
print("Number of Ts")
print(userSeq.lower().count("t"))

# DB: Good! My only suggestion is that you can make it more general by allowing both
#     upper- and lowercase sequences if you add .lower() to userSeq (see above).