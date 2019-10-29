#!usr/bin/python3

def birthdayCakeCandles(arr):
    numberOfTallestCandle = 0
    tallestCandle = max(arr)

    print('tallest candle:', tallestCandle)

    for x in range(len(arr)):
        if arr[x] == tallestCandle:
            numberOfTallestCandle = numberOfTallestCandle + 1
        else:
            pass

    print('there are', numberOfTallestCandle, 'tallest candle(s) on the cake')


a = [4, 4, 1, 2, 5, 6, 1, 2, 4, 6, 8]

birthdayCakeCandles(a)
