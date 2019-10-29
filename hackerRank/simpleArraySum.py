#https://www.hackerrank.com/challenges/simple-array-sum/problem

#!usr/bin/python3

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(n):
    sum = 0
    arr = [0 for x in range(n)]
    #arr[0] = 1
    #print('sum1: ', sum1)

    for x in range(n):
        arr[x] = x*3

        temp = arr[x]
        print("arr[",x,"] = ", arr[x])
        sum = sum + temp

    print("sum of array:", sum)

simpleArraySum(5)