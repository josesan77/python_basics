# -*- coding: utf-8 -*-
"""
Created on 2024-06-18 15:15:15
Level 'easy' problem defined on GeeksForGeeks website. The code below was accepted as solution.
https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/0

Copied from GeeksForGeeks:
"Given a positive integer n, find the nth fibonacci number. Since the answer can be very large, return the answer modulo 1000000007.
Note: for the reference of this question take first fibonacci number to be 1.
----------------------------------------------------
Examples :
1) Input: n = 2
Output: 1 
Explanation: 1 is the 2nd number of fibonacci series.
2) Input: n = 5
Output: 5
Explanation: 5 is the 5th number of fibonacci series.
------------------------------
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1<= n <=10^5  "

@author: josesan77
"""

def nthFibonacci( n : int) -> int:
    mod_base = 10**9 +7 #for easier printing at high numbers
    if n < 3:
        return 1
    arr1, arr2 = 0, 1
    for _ in range(2, n+1, 1):
        new_item = (arr1 + arr2) % mod_base
        arr1, arr2 = arr2, new_item
    return arr2

n = 10
print('Serie element #' + str(n) + ' : ' + str(nthFibonacci(n)))