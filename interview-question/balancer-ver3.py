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
flag = True

def balance(arr):

    pair1 = ['(', ')']
    pair2 = ['{', '}']
    pair3 = ['[', ']']
    index1 = 0
    index2 = 1

    #print('length of arr:', len(arr))
    x = int(len(arr)/2)
    

    #print('length:', x)
    #print(arr[x])

    for n in range(x):
        #print(n)
        #print(x-1-n, '=', arr[x-1-n], end=' - ') #print the first half of the array
        #print(x+n, '=', arr[x+n], end=' - ') # print the second half of the array

        if arr[x-1-n] == pair1[0] and arr[x+n] == pair1[1]:
            #print(arr[x-1-n] + arr[x+n], '- Valid a') # pair of ()
            flag = True
            display_result(flag)
        elif arr[x-1-n] == pair2[0] and arr[x+n] == pair2[1]: 
            #print(arr[x-1-n] + arr[x+n], '- Valid b') # pair of {}
            flag = True
            display_result(flag)
        elif arr[x-1-n] == pair3[0] and arr[x+n] == pair3[1]:
            #print(arr[x-1-n] + arr[x+n], '- Valid c') # pair of []
            flag = True
            display_result(flag)

        elif arr[n+index1] == pair1[0] and arr[n+index2] == pair1[1]:
            #print(arr[n+index1] + arr[n+index2], '- Valid x') # pair of ()
            flag = True
            display_result(flag)
        elif arr[n+index1] == pair2[0] and arr[n+index2] == pair2[1]:
            print(arr[n+index1] + arr[n+index2], '- Valid y') # pair of {}
            flag = True
            display_result(flag)
        elif arr[n+index1] == pair3[0] and arr[n+index2] == pair3[1]:
            #print(arr[n+index1] + arr[n+index2], '- Valid z') # pair of []
            flag = True
            display_result(flag)
        else:
            #print('Not valid')
            flag = False
            display_result(flag)

        index1 = index1 + 1
        index2 = index1 + 1
        #print('index1 =', index1)
        #print('index2 =', index2)
        #print('[',x-1-n,']:',arr[x-1-n], end='')
        #print(arr[x-1-n], end='')

def display_result(f):
    if f == False:
        print('Valid:', f)
        exit
    else:
        print('Valid:', f)

#display_result(flag)

# Test cases:
#x = ['',''] # not valid
#x = ['(',')'] # valid
#x = ['[',']'] # valid
#x = ['(',')','{','}'] # valid
#x = ['{','}'] # not valid
#x = ['(','[',')',']'] # not valid
#x = ['{','(','[',']',')','}'] # valid
#x = ['{','[',')','}','(',']'] # not valid
x = [';','{','}',':'] # not valid

balance(x)