#!usr/bin/python3
#this app is pretty buggy. currently it works only with PM

def timeConversion(s):
    newString = s.split(':')
    am = newString[2].split('AM')
    pm = newString[2].split('PM')

    print(newString)
    #print(newString[2])

    #print(am)
    print(pm)
    print(pm[1])

    if pm[1] == '': #if '' means this is PM
        hour = int(newString[0]) + 12
        #print(hour)
        print(str(hour)+':'+newString[1]+':'+ pm[0])
    else:

        print('it is AM')


timeConversion('09:01:43PM')