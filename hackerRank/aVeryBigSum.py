#!usr/bin/python3

def aVeryBigSum(ar):

    sum = 0

    for x in range(len(ar)):
        temp = 0
        temp = ar[x]
        sum = sum + temp
    
    print("Sum of array is", sum)

a = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 9000000005]

aVeryBigSum(a)