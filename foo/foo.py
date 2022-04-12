# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 00:05:00 2022

@author: Patri
"""

def is_divisible_by_k(x,k):
    '''
    Checks wether x is divisble by k.
    '''
    
    '''
    ## Changed assertion, checking if number >= 0
    '''
    assert x >= 0
    assert k >= 0
    '''
    ## Added return statement.
    ## If bitwise operators are used, dont forget to use brackets ... 
    ## Assuming we dont want 0
    '''
    if x % k == 0 and x > 0:
        return(True)
    else:
        return(False)

'''
Store all integers that are multiples of 2, 5 or 7 that are lower or equal to 1000 (excluding doubles)
## Changed Tuple to List, as tuple doesnt have an append method
'''

x = []
for i in range(1000):
    '''
    ## Changed bitwise operators to or
    ## Changed divisor 3 to 5
    ## Changed x to i
    '''
    if is_divisible_by_k(i,2) or is_divisible_by_k(i,5) or is_divisible_by_k(i,7):
        x.append(i)

'''
Sum all integers that are multiples of 2, 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''

print(sum(x))
