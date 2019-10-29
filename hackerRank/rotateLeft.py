"""A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

An array of integers .
An integer , the number of rotations.
Input Format

The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
The second line contains  space-separated integers .

Constraints

Output Format

Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5 """

def rotateLeft(a, d):
    n = len(a)
    r = n-d
    b = []
    print("length of the array:", len(a))
    print('array:', a)
    print("rotation:", d)
    print()

    for x in range(d):
        b.append(a[x])

    print('b =', b)

    for i in range(r):
        a[i] = a[i+d]

    print('new a =', a)
    
    for k in range(d):
        a[k+1] = a[k+1]
    
    for m in range(d):
        a[m+r] = b[m]

    print('final a =:', a)
        


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

rotateLeft(arr, 5)