# -*- coding: utf-8 -*-
"""
Section 5
"""
#Days of the Month

Months ={
1:["January", 31],
2:["February", 28],
3:["March", 31],
4:["April", 30],
5:["May", 31],
6:["June", 30],
7:["July", 31],
8:["August", 31],
9:["September", 30],
10:["October", 31],
11:["November", 30],
12:["December", 31] 
}

value = list(Months.values())
while True:
    try:numM = int(("Please enter a month(1-12)"))
    except:
        print("Input a Number please:")
        continue
    
    if numM <1 or numM >12:
        print ("Enter a digit between 1-12:")
        continue
    else:
        break
    
        
        