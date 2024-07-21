# -*- coding: utf-8 -*-
"""
Created on Mon Jul 8 22:47:22 2024
Level 'easy' problem defined on GeeksForGeeks website. See details:
    https://www.geeksforgeeks.org/problems/fibonacci-series-up-to-nth-term/1
The code below was accepted as solution.

Fibonacci series up to Nth term
Difficulty: Easy Accuracy: 51.0% Submissions: 49K+ Points: 2
You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. Since the terms can become very large return the terms modulo 109+7.

Example 1:

Input:
n = 5
Output:
0 1 1 2 3 5
Explanation:
0 1 1 2 3 5 is the Fibonacci series up to the 5th term.

@author: josesan77
"""

def fibonacci_serie(n : int) -> int:
    if n > 50:
        print('Serie element number restricted to 50. Modify the limit on your on responsibility.')
    fibonacci_serie = [0, 1] #initial two elements in the serie
    mod_base = 10**9 +7 # for large number simplified printing
    arr1, arr2 = 0, 1
    for _ in range(2, n+1, 1):
        new_item = (arr1 + arr2) % mod_base
        arr1, arr2 = arr2, new_item
        fibonacci_serie.append(new_item)
    return fibonacci_serie

n = 10
print('Serie element #' + str(n) + ' : ' + str(fibonacci_serie(n)))