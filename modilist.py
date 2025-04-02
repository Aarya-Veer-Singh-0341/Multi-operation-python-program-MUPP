from time import *
def modilist():
    mainlist = []
    print("\nPress enter to end the list\n")
    for i in range(50):
        inputlistone = input("Enter Element:")
        if inputlistone == "":
            break
        mainlist.append(inputlistone)
        print(mainlist)
    sleep(0.3)
    print("List is:",mainlist)
    sleep(0.3)
    print("\nTHESE ARE THE MODIFICATION\n--------------------------------\n")
    print("Reversed list:",mainlist[::-1])
    sleep(0.5)
    print("\nHASHING OF EACH ELEMENT:\n---------------------------")
    for i in range(len(mainlist)):
        hashlist = []
        hashed = mainlist[i]
        hashed = hash(hashed)
        hashlist.append(hashed)
        print(mainlist[i],":",hashlist)