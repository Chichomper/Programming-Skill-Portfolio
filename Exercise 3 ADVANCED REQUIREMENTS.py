# -*- coding: utf-8 -*-
"""
Section 3
"""
#BIOGRAPHY

info = {
    "Name" : "Cian",
    "Age" : 17,
    "Home" : "Dubai"
    }
for key, value in info.items():
    print (key, value)
    
#ADVANCED REQUIREMENT

while True:
    Name = input("Enter First Name:")
    count = len(Name.split())
    if count > 1:
        print("I appears you have entered more than your first name")
        print("please type your name in again")
        continue
    else:
        break
    
    while True:
        try:
            Age = int(input("input your age here: "))
            break
        except:
            print("Please enter your age, these are simply words, idiot")
            
            Home = input("Enter your Home: ")
            print("Your Home:", Home)
            print("Your Age:", Age)
            print("Your Name:", Name)