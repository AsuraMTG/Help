import math
import random
import datetime

def three():
    
    for item in list:
        p=len(item.n.split(' '))
        if p > 2 :   
            print(f"Yes this: ")
            print(f"\t\t {item.n}")
        #elif db<=2:    
        #else:
            print(F"\t3.f. Nincs ilyen személy.")

def plus(): 
    
    plus = ""
    for item in list:
        plus += item.a + " "
    print("--)a + a .")
    print(plus)

def part():
    part= "esz"
    p=0
    for item in list:
        if part in item:
            print(item)
            p+=1
    print(p)


def password2():
    user="cba33"
    passw = "abc"
    while True:
        newuser=input("?user!: ")
        newpassw=input("?passw!: ")
        if newuser == user and newpassw == passw:
            print("OK.")
            break
        else:
            print("Stay out.")

#----------------------------

def wordsand():
    word= input("word!")
    word= word.lower()
    n = the(word)
    j = plus()
    print(n, word, j)


def plus():
    plus = ["piros", "lila", "zöld","fekete", "fehér"]
    return random.choice(plus)

#paraméterlista
def the(word):
    mgh= "aáeéiíoóöőuúüű"
    
    if word[0] in mgh:
        return "Az"
    else:
        return "A"  

#----------------------------

def f2_kedvencfilm():

    for _ in range(3):
        film = input("Kérem a film címét: ")
        idotart = int(input("Kérem a film hosszát percben: ") )
        
        ora = idotart//60
        print(ora)
        perc = idotart - ora * 60
        print(perc)
    
        print(f"A(z) {film} című film {ora} óra {perc} perc hosszú.")

def f2_oraperc(ido):

        ora = ido//60
        perc = ido - ora * 60
      
        return str(ora) + ':' + str(perc) 

def f2_kedvencfilm2():    
    
    for _ in range(1):
        film = input("Kérem a film címét: ")
        idotart = int(input("Kérem a film hosszát percben: ") )
           
        print(f"A(z) {film} című film, {f2_oraperc(idotart)} hosszú.")














