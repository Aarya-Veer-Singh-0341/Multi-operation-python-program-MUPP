def prime():
    primenum = int(input("Enter Number:"))
    if primenum < 0:
        print("Give correct value")
    elif primenum == 1:
        print("1 is neither composite nor prime")
    elif primenum == 2:
        print("prime")
    for i in range(2,primenum):
        if primenum % i == 0:
            print("normal")
            break
        elif i == primenum-1:
            print("prime")
        