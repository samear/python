"""
This is the first programing test for salesforce.

Given a matrix of distinct values and a sum.
The task is to print the number of pairs whose summation is equal to given sum.
Each element of pair must be from different rows (i.e., a pair must not lie in the same row). If there is not possible pair print "No Output"
Sample Input:
Sum = 3
[[1,0],
[-1,2]]
Sample Output: 1
"""
def pairs(sum, matrix):
    i = 0
    ii = 0
    x = 0
    n = 0
    m = 0
    print("lengh of matrix", len(matrix))
    #print(sum, matrix)
    #count = 0
    #print('length', len(matrix))
    #print(matrix[0][0]) #= 1
    #print(matrix[0][1]) #= 0
    #print(matrix[0][2])
    #print(matrix[0][3])
    #print(matrix[5][1])
    #print(matrix[3][3])
    #print(matrix[1][0]) #= -1
    #print(matrix[1][1]) #= 2
    print("====")

    if matrix[0][0] + matrix[1][1] == 3:
        print("yes")
    else:
        print("no")

    s1 = 0

    for i in range(len(matrix)-1):
        for x in range(len(matrix)):
            if i <= len(matrix):
                print("[",matrix[s1][i], "+", matrix[i+1][x],"]",end=" ")
            else:
                s1  = s1 + 1
                print("inscreasing s1")

s = 3
""" m = [[1,0],
     [-1,2]] """

m = [[1,0,2,4,7,8],
    [-1,2,4,5,6,9],
    [-2,1,0,8,9,3],
    [-3,7,6,5,0,1],
    [-6,7,9,2,3,4],
    [-5,4,3,2,1,8]]

print(pairs(s, m))