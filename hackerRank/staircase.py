#!usr/bin/python3

def stairCase(n):

    step = "#"
    for x in range(n+1):
        print(step*x)

stairCase(int(input("Enter a number:")))