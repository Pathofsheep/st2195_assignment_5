# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 00:05:00 2022

@author: Patri
"""

def is_divisible_by_k(x,k):
    # Checks wether x is divisble by k.
    # Removed Assert
    # Added return statement.
    # If bitwise operators are used, dont forget to use brackets ... 
    
    if x % k == 0:
        return(True)
    else:
        return(False)

'''
Store all integers that are multiples of 2, 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''
# Changed Tuple to List, as tuple doesnt have an append method
# Changed range to 1001

x = []
for i in range(1001):
    
    # Changed bitwise operators to or
    # Changed divisor 3 to 5
    # Changed x to i
    
    if is_divisible_by_k(i,2) or is_divisible_by_k(i,5) or is_divisible_by_k(i,7):
        x.append(i)

'''
Sum all integers that are multiples of 2, 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''

print(sum(x))
