def makeAnagram(a, b):
    print("a = ", a)
    print('b = ', b)

    count = 0

    for i in range(len(a)):
        for x in range(len(b)):
            if a[i] == b[x]:
                count = count + 1
            else:
                print(a[i], '=', b[i])

    print('number of delete:', len(a) + len(b) - count*2 )
x = 'cde'
y = 'abe'

makeAnagram(x, y)