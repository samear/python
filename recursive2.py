# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:23:17 2019

@author: sam
"""

def factorial(n):
    f=1
    while n>0:
        f*=n
        n-=1
    print(f)
    
n = int(input("enter the number :"))
factorial(n)