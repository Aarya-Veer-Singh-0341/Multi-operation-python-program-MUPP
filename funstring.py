from time import sleep
def basicstring(mainstr,strinputone):
    
    if strinputone == int(1) or strinputone == (0):
        palinstr = mainstr
        palinstr = palinstr.lower()
        palinstr = palinstr.replace(" ","")

        palinhalf = (len(palinstr)/2)
        if (10*palinhalf) % 2 != 0:
            palinhalf -= 0.5
            palinhalf = int(palinhalf)
        else:
            palinhalf = int(palinhalf)

        if len(palinstr) % 2 != 0:
            palinstr = palinstr[:palinhalf]+ palinstr[palinhalf+1:] 
        palinrev = palinstr[palinhalf:]
        if palinstr[:palinhalf] == palinrev[::-1] :
            print("\nITS A PALINDROME!")
        else:
            print("\nITS NOT A PALINDROME!")
    if strinputone == (2)or strinputone == (0):
        sleep(0.25)
        print("\nReveresed string:",mainstr[::-1])
        fixedstr = mainstr.lower()
        fixedstr = fixedstr.capitalize()
        sleep(0.25)
        print('\nFixed String:',fixedstr)
    if strinputone > 2:
        sleep(0.25)
        print("\nWrong entry!!")