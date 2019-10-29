#!usr/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):

    alicepoint = 0
    bobpoint = 0

    for x in range(3):
        if a[x] > b[x]:
            alicepoint = alicepoint+1
            print("Alice has", a[x], "- Alice gets", alicepoint)
        elif a[x] == b[x]:
            print('love')
        else:
            bobpoint = bobpoint + 1
            print("Bob has", b[x], "- Bob gets", bobpoint)
   
    print("Total point for Alice", alicepoint)
    print("Total point for Bob", bobpoint)

x = [1, 200, 3]
y = [3, 2, 5]

compareTriplets(x, y)