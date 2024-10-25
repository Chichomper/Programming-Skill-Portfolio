# -*- coding: utf-8 -*-
"""
Section 10
"""
#EVEN  OR ODD

def evenOrodd(Num):
    if Num % 2 == 0:
        print (f"the number {Num} is even")
        print (f"the number {Num} is odd")
        
def main():
    while True:
        try:
            Inputnum = int(input("Enter the desired number:"))
            break
        except:
            print ("That ids not a number, dumba-")
            
        resultNum = evenOrodd(Inputnum)
        print (resultNum)
        
if __name__ == "__main__":
    main()
        


