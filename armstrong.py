def arm():
    armlist = []
    armnum = int(input("Enter Number:"))
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
arm()
