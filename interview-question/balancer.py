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

    if arr[0] == pair1[1] or arr[0] == pair2[1] or arr[0] == pair3[1]:
        print('Not valid')
    else:    

        for i in range(len(arr)):
            if arr[i] == pair1[0]:
                if arr[1] == pair1[1]:
                    print('Valid')
                else:
                    print('Not valid')
            elif arr[i] == pair2[0]:
                if arr[1] == pair2[1]:
                    print('Valid')
                else:
                    print('Not valid')
            elif arr[i] == pair3[0]:
                if arr[1] == pair3[1]:
                    print('Valid')
                else:
                    print('Not valid')

x = ['{','}']

balance(x)