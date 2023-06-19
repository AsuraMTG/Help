import random

def vi():

    ne = 0
    po = 0
    while ne != "":  # end = enter
        ne = input("ne: ")
        if ne ==  "":
            print("end")
        else:
            po = int(input("po: "))
            print(f"{ne} aaa {pon(po)}, {je2()}")

def je2():

    je= ["p", "l", "z","f", "f"]
    return random.choice(je)

def pon(po):
    
    if po >= 48:
        return "+"
    else:
        return "-"  

def main():
    vi()

main()    

#*******************

import random
def fon():
    
    for i in range(3):
        f = input("f: ")
        print(f"\t {ne(f)} {f} {je()}. ")
        f= f.lower()

def je():

    je= ["a", "b", "c","d", "e"]
    return random.choice(je)

def ne(f):  

    mgh= "aáeéiíoóöőuúüű"
    if f[0] in mgh:
        return "Az"
    else:
        return "A"    
#******************    
