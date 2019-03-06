# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:53:11 2019

@author: sam
Purpose: Recursive Function Python – Learn Python Recursion with Example
https://www.simplifiedpython.net/recursive-function-python/
"""

def fact(n):
    if n==0 :
        return 1
    else:
        return n*fact(n-1)
 
n = int(input("enter the number :"))
result = fact(n)
print("Factorial of",n,"is",result)

