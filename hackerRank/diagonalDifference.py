#!usr/bin/python3

def diagonalDifference(arr):
    dif = 0
    temp1 = arr[0][0]+arr[1][1]+arr[2][2]
    temp2 = arr[0][2]+arr[1][1]+arr[2][0]
    diff = temp1 - temp2

    print(arr[2][2])

    print('length of array:', len(arr))
    print('temp1 =', temp1)
    print('temp2 =', temp2)
    print('sum = ', diff)
    print('absolute value of diagonal = ', abs(diff))

a = [[11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]]

diagonalDifference(a)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       