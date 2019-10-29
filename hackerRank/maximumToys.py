def maximumToys(prices, k):

    arr = [1, 12, 111, 3, 200, 1000, 10]
    count = 0
    total = 0

    print('there are', prices, 'prices')
    print('Mark can spend up to $', k)
    print()

    for i in range(len(arr)):
        if arr[i] <= k:
            count = count + 1
            total = total + arr[i]
            if total >= k:
                count = count -1
                break
                
                
    print('Number of piece(s) Mak can buy:', count)
    print('These piece(s) are worth: $' + str(total))

maximumToys(7, 50)