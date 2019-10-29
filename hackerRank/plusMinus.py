#!usr/bin/python3

def plusMinus(arr):
    zero = 0
    neg = 0
    pos = 0

    for x in range(len(arr)):
        if arr[x] == 0:
            zero = zero + 1
            #print('Numberof zero:', zerro)
        elif arr[x] < 1:
            neg = neg +1
            #print('Numberof negative:', neg)
        else:
            pos = pos +1
            #print('Number of positive:', pos)

    print('Numberof zero:', zero)
    print('Numberof negative:', neg)
    print('Number of positive:', pos)

    zeroRatio = zero/len(arr)
    negRatio = neg/len(arr)

    posRatio = pos/len(arr)

    print('zero ratio:','{0:.6f}'.format(zeroRatio))
    print('negative ratio:','{0:.6f}'.format(negRatio))
    print('positive ratio:','{0:.6f}'.format(posRatio))


a = [-4, 3, -9, 0, 4, 1]

plusMinus(a)