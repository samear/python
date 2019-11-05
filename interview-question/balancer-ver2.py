"""
This is programing test for salesforce

A string which contain only the characters '(', ')', '{','}', '[' and ']' is considered valid, if all
the brackets are closed in the correct order.
for example, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Given an array of several string as the input, print "Valid" or "Not valid" on separate lines for each
input string.
If the input string contains any characters other than '(', ')', '{', '}', '[' and ']', then just
print "Not valid". Empty string are always valid.
Test cases:
i/p -> Empty string: valid
i/p -> (): valid
i/p -> []: valid
i/p -> (){}: valid
i/p -> {]: Not valid
i/p -> ([)]: Not valid
i/p -> {([])}: valid
i/p -> {[)}(]: not valid
i/p -> ;{}: not valid
"""
def balance(arr):

    pair1 = ['(', ')']
    pair2 = ['{', '}']
    pair3 = ['[', ']']

    #print('length of arr:', len(arr))
    x = int(len(arr)/2)

    #print('length:', x)
    #print(arr[x])

    for n in range(x):
        #print(n)
        #print(x-1-n, '=', arr[x-1-n], end=' - ') #print the first half of the array
        #print(x+n, '=', arr[x+n], end=' - ') # print the second half of the array
        
        if arr[x-1-n] == pair1[0] or arr[x-1-n] == pair2[0] or arr[x-1-n] == pair3[0]:
            print('Valid - [',x-1-n,']:',arr[x-1-n])
            if arr[x+n] == pair1[1]:
                print('Valid')
            else:
                print('Not valid')
        else:
            print('Not valid')
        

x = ['(','{','[','(',')',']','}',')']

balance(x)