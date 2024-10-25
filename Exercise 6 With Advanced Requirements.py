# -*- coding: utf-8 -*-
"""
section 6
"""
#Brute Force Attack

correctpassword = "54321"
attempts = 5

while True:
    passInput = input ("Enter your Password here:")
    if passInput == "54321":
        print ("Password Identified, Please go ahead")
        break
    else: #Following is the advanced requirements
         print (f"incorrect Password, you have {attempts} left, please reenter")
         attempts -= 1
         if attempts < 0:
             print ("Congrats, you have alerted the authorities, have fun!")
             break
         continue
             



    
          
    

