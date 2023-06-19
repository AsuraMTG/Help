import math
import random
import datetime


def f_p(): 

    for item in list:
        if item.n == "AB":
            print(f"Ther is.")    
            break
    else:
        print(f"Not.")  

def change(): 
    a=int(input("1: "))
    b=int(input("2: "))
    l=int(input("L: "))
    c = 0
    d = 0
    print(f"1: {a}, 2:{b}")
       
    if a>b:  # making c=0, d=0 and change!
        c = b
        d = a
    else:
        c = a
        d = b
           
    for i in range(c,d + 1,l):
        print(i, end=" ")

def w(): 
    
    rep=True
    while rep:
        a=float(input("k e sz: "))    
        b=float(input("k e sz: ")) 
        if a >b :
            print("A > b")
        elif a<b :
            print("A < b")
        else:    
            print(" a= B")
            rep=False

    a=2
    b=3 
    while a!=b:
        a=float(input("k e sz: "))    
        b=float(input("k e sz: ")) 
        if a >b :
            print("A > b")
        elif a<b :
            print("A < b")
        else:    
            print(" a= B")
    
    while True:
        a=float(input("k e sz: "))    
        b=float(input("k e sz: ")) 
        if a >b :
            print("A > b")
        elif a<b :
            print("A < b")
        else:    
            print(" a= B")
            break

def gift(): 
    
    giftnumb = len(list)
    ajanlas=random.randint(0, giftnumb+1)
    return list[gift]

def gift2():

    print(f"AAA {gift().strip()} aaa.")

def forelse():
   
    n=input("???: ")
    for item in list:
        if n in item.n:
            print("Yes")
    else:
        print("Not")

def double(): # not

    double = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                double.append(list[i]) 
                print(*double)    
    print(f"double: n, érik el vagy haladják meg az 1 tonnát.")

def upDown(): 

    e=float(input("K 1.:"))
    print(f"1 {math.floor(e)} and {math.ceil(e)} between {round(e)} near.")
    print(f"whole: {e//1}")
    print(f"/: {round(e%1,2)}")

def szetvalaszt():
    
    list = []
    n = []
    t = []
    
    for item in list:
        reszek= item.split(";")
        print(reszek[0], " - " ,reszek[1])
        n.append(reszek[0])
        t.append(reszek[1])

















