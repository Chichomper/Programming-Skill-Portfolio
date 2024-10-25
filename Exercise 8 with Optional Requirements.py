# -*- coding: utf-8 -*-
"""
Section 8
"""
#SIMPLE SEARCH

NameList = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
print (NameList[4])#this'll print Sam, being the 5th name, as indexes will always start at 0
"""
OPTIONAL REQUIREMENTS
"""

print(NameList)
while True:
    try:
        Nameinput = int(input("Pleasae enter number of the participant corresponding to the placement:"))
    except:
        print ("Please re-enter the position for the number:")
        continue
    if Nameinput <1 or Nameinput >6:
        print ("Enter a Nummber between 1-6, please")
        continue
    else:
        break
#This code will search up the name of the person 
print (f"the one you're looking for is {NameList[Nameinput-1]}")

        
            

