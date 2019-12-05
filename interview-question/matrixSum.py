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
    #print(sum, matrix)
    #count = 0
    #print('length', len(matrix))
    #print(matrix[0][0]) #= 1
    #print(matrix[0][1]) = 0
    #print(matrix[1][0]) #= -1
    #print(matrix[1][1]) #= 2
    print("====")


    """ for i in range(len(matrix)):
        for x in range(len(matrix) - 1):
            #print(matrix[x][i])

            if matrix[x][x] + matrix[i][i] == sum:
                count = count + 1
            else:
                print('No Output')

    return count """

    for i in range(len(matrix)):
        for n in range(len(matrix)):
            print(matrix[i][n])
            if matrix[i][n] + matrix[i][n]== sum:
                print("sum =", sum)




s = 3
m = [[1,0],
    [-1,2]]

print(pairs(s, m))