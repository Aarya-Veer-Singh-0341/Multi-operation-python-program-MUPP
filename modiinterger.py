from statistics import *

def binary(mainint):
    denominator = 2
    binarylist = []
    qoutient = mainint // denominator
    remainder = mainint % denominator
    while qoutient != 0:
        binarylist.append(int(remainder))
        mainint = qoutient 
        qoutient = mainint // denominator
        remainder = mainint % denominator
    binarylist.append(int(1))
    binarylist = binarylist[::-1]
    print("Binary code for",mainint,"is:",binarylist)


def hexa(mainint):
    denominator = 16
    hexalist = []
    qoutient = mainint // denominator
    remainder = mainint % denominator
    while remainder != 0:
        hexalist.append(int(remainder))
        mainint = qoutient 
        qoutient = mainint // denominator
        remainder = mainint % denominator
    for i in range(len(hexalist)):
        if hexalist[i] == 10:
            hexalist[i] = 'A'
        if hexalist[i] == 11:
            hexalist[i] = 'B'
        if hexalist[i] == 12:
            hexalist[i] = 'C'
        if hexalist[i] == 13:
            hexalist[i] = 'D'
        if hexalist[i] == 14:
            hexalist[i] = 'E'
        if hexalist[i] == 10:
            hexalist[i] = 'F'            
    hexalist = hexalist[::-1]
    print("Hexadecimal code for",mainint,"is:",hexalist)

def arm(mainint):
    armlist = []
    armnum = mainint
    size = len(str(armnum))
    add = 0
    for t in range(size):
        a1 = (int((str(armnum)[t]))**size)
        b2 = a1
        c3 = b2
        armlist.append(c3)
    for j in range(len(armlist)):
        add += armlist[j]
    if add == armnum:
        print("Yes,it is a armstrong number")
    else:
        print("No,It is not a armstrong number")


def prime(mainint):
    if mainint > 1:
        for i in range(2, (mainint//2)+1):
            if (mainint% i) == 0:
                print(mainint, "is not a prime number")
                break
        else:
            print(mainint, "is a prime mainintber")
    else:
        print(mainint, "is not a prime number")


def basiccalc():
    numlist = []
    InputAmoutOfNum = int(input("How many number will you input: "))
    for i in range(InputAmoutOfNum):
        InputNumEach = int(input("Enter Number:"))
        numlist.append(InputNumEach)
    print(numlist)
    print("\nNOW LETS OPERATE THEM\n----------------------")
    addhold = 0
    for val in numlist:
        addhold += val
    print(addhold)
    mulhold = 1
    for val in numlist:
        mulhold =  mulhold*val
    print(mulhold)
    size = len(numlist)
    print("mean:",mean(numlist))
    print("mode:",mode(numlist))
    print("median:",median(numlist))