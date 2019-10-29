#python program for implementation of buble sort
#geeksforgeeks.org/bubble-sort

def bubbleSort(arr):

    temp = 0
    n = len(arr)
    print('length of array:', n)
    print('original array:', arr)

    #traverse through all array elements

    for i in range(n):

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print()

    print('sorted array:', arr)

a = [5, 2,4,7,10,7, 2, 4,6,1,9,8,3]

bubbleSort(a)
