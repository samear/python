#!usr/bin/python3

def miniMaxSum(arr):

    temp = 0
    tempMin = 0
    tempMax = 0
    sum = 0
    minValue = min(arr)
    maxValue = max(arr)

    print('array:', arr)
    print("smallest value in the array: ", minValue)
    print("biggest value in the array:", maxValue)

    for x in range(len(arr)):
        tempMin = min(arr)
        tempMax = max(arr)
        temp = arr[x]
        sum = sum + temp

    

    print('sum of the array without minimum value:',sum - tempMin)
    print('sum of array without maximum value:', sum - tempMax)

a = [10, 21,35, 49, 50]

miniMaxSum(a)