# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 22:19:20 2024
********* ARMSTRONG NUMBERS ***********
https://www.geeksforgeeks.org/problems/armstrong-numbers2727/0

Copied from website:
    "
    You are given a 3-digit number n, Find whether it is an Armstrong number or not.

    An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 
    
    Note: Return "true" if it is an Armstrong number else return "false".
    
    Examples
    
    Input: n = 153
    Output: true
    Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153. Hence answer is "true".
    Input: n = 372
    Output: false
    Explanation: 372 is not an Armstrong number since 33 + 73 + 23 = 378. Hence answer is "false".
    Expected Time Complexity: O(1)
    Expected Auxiliary Space: O(1) 
    
    Constraints:
    100 ≤ n <1000 
    "

@author: josesan77
"""

def armstrongNumber(n):
    digits_cube_list = [int(x)**3 for x in str(n)]
    sum_cubes = sum(digits_cube_list)
    if sum_cubes == n:
        return 'Yes'
    else:
        return 'No'

# call function
n = 153
answer = armstrongNumber( n)
print(answer)