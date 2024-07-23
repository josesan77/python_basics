# -*- coding: utf-8 -*-
"""
******* PADOVAN SEQUENCE problem *******
https://en.wikipedia.org/wiki/Padovan_sequence

problem defined on GeeksForGeeks:
https://www.geeksforgeeks.org/problems/padovan-sequence2855/1

Copied from website:
"
Given a number n, find the nth number in the Padovan Sequence.

A Padovan Sequence is a sequence which is represented by the following recurrence relation
P(n) = P(n-2) + P(n-3)
P(0) = P(1) = P(2) = 1

Note: Since the output may be too large, compute the answer modulo 10^9+7.

Examples :

Input: n = 3
Output: 2
Explanation: We already know, P1 + P0 = P3 and P1 = 1 and P0 = 1
Input: n = 4
Output: 2
Explanation: We already know, P4  = P2 + P1 and P2 = 1 and P1 = 1
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
"

@author: josesan77
Created on Wed Jun 12 22:25:35 2024
"""
def padovanSequence_basic(n): # does not succeed under critical time limit 1.68 sec

    mod_base = 10**9 +7 #GFG requested for easier presentation of large numbers
    arr = [1, 1, 1]
    if n < 3:
        return arr[n]
    for i in range(3,n+1):
        arr.append((arr[i-2] + arr[i-3]) % mod_base)
    return arr[n]
    
# fast processing solution
def padovanSequence(n):
    
    mod_base = 10**9 +7#GFG requested for easier presentation of large numbers
    if n < 3:
        return 1
    arr1, arr2, arr3 = 1, 1, 1
    for _ in range(3, n+1, 1):
        new_item = (arr1 + arr2) % mod_base
        arr1, arr2, arr3 = arr2, arr3, new_item
    return arr3

# call function
# nth_element = padovanSequence(10)