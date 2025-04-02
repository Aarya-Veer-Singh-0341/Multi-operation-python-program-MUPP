from modilist import *
from funstring import *
from modiinterger import *
from statistics import *
from time import *

print("Hello,welcome to MUPP,\nMulti Operation Python Programme\n")
maininput = int(input("What would you like to work with?\n 1.Lists \n 2.Integers \n 3.Strings\n"))
if maininput == 1:
    sleep(0.2)
    modilist()
elif maininput == 2:
    sleep(0.2)
    print("\nWELCOME TO MODIFYING INTEGERS\n-------------------------\nWhat would you like to do?\n")
    mainintinput = int(input("1.Basic calculation:\n2.Something FUN:\n"))
    if maininput == 1:
        basiccalc()
    elif maininput == 2:
        maininput = int(input("Enter a number:"))
        sleep(0.25)
        prime(maininput)
        sleep(0.25)
        binary(maininput)
        sleep(0.25)
        hexa(maininput)
        sleep(0.25)
        arm(maininput)
elif maininput == 3:
    maintstr = input("Enter a string for operation:")
    strinputone = int(input("Select what to do:\n1.Check for palindromes:\n2.Reverse it!:\n0.BOTH OF THE ABOVE!\n"))
    basicstring(maintstr,strinputone)
else:
    print("incorrect entry")