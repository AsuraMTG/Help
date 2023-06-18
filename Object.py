import math
import random
import datetime

class Class:
    def __init__(self, a, b, c, d, e, f):
        
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def abc(self):
        return self.d * 2

    def points(self):      
        if points != 0:
            points=float(self.a)+float(self.b)-float(self.d)
            return points
        elif points> 1000:
            return 0

    def age(self):
        return 2023-self.birth 

list=[]

def read():
    f=open(" .txt", encoding="UTF-8")
    f.readline() # first row
  
    for row in f:
        part=row.strip().split(";") #("\t" if space)
        a = part[0]
        b = part[1]
        c = part[2]
        d = int(part[3])
        e = part[4]
        f = int(part[5])
        obj = Class(a, b, c, d, e, f)
        list.append(obj)
	
    f.close() 

def print():
    for item in list:
        print(item.a, item.b, item.c, item.d, item.e, item.f)
		
def entry(): 

    f=open(" .txt", "w", encoding="UTF-8")   
    for item in list:
        if float(item.c) > 1000 or float(item.d) > 1000:
            this= f"{item.a}, {item.b()}\n"
            f.write(this)
    f.close() 

def main():
    read()
main()    

list=[]

def justReading():
    f= open(" .txt", encoding="UTF-8") 
    for row in f:
        list.append(row)

    for item in list:
        print(item)
    print("AAAAA")  

#**********************
     
def sets():

    sets=set([])
    for item in list:
        sets.add(item.a)

    for item in sets:
        print(sets)
    print(*sets)

#////////////////

def leg():
    leg=list[0]
    for item in list:
        if leg.b < item.b:
           leg=item
    print(f"AAAAAAAAAAA: ")
    print(f"\tA:{leg.a}")
    print(f"\tB:{leg.b}")
    print(f"\tC:{leg.c}")
    print(f"\tD:{leg.d}")    

def younger():
    young=list[0]
    for item in list:
        if young.age()>item.age():   # > less < more 
            young=item
    print("young")  

def olders():                   
    older=[]
    for item in list:
        if item.age() < item.age():
            older.append(item)
    
    leg=older[0]
    for item in older:
        if leg.age() < item.age():
           leg=item
    print(f"AAAAAAAAAAA: ")
    print(f"\tA:{leg.a}")
    print(f"\tB:{leg.b}")
    print(f"\tC:{leg.c}")
    print(f"\tD:{leg.d}") 

    print(f"leg>: {max(older)}")
    print(f"leg<: {min(older)}")  
#////////////////

def avg():
    kg=0
    for item in list:
        kg += item.kg
    avg=round(kg/len(list),1)
    print(f"AAAAAAAAAA:{avg} m")

def vane():
    
    vane=False
    a=int(input("???: "))
    for item in list:
        if item.m == "B" and item.m > a:
            print(f"\tAAA {a} < m in B.")
            vane=True
            break
    else:
        print(f"\tBBB {a} < m  in B. ")    

def place(): 
    
    print(f"first {list[0].a}, and {list[0].b}, last {list[-1].a}, and {list[-1].b}")	

def rk():  # not in

    rk=[]
    print("CCC:")
    for item in list:
        if item.r not in rk:
            rk.append(item.c)
    print(*rk)

def tg():
    for item in list:
        if item.t < item.g:
            print(f"{item.n}: {item.g - item.t+1}")
        else:
            honap= (12- item.tol) + item.g +1
            print(f"{item.n}: {honap}")	

def piece():
    p=0
    for item in list:
        if item.t == "t" and item.n == "m":
            p+=1      
    print(f"AAAAA {p} p m t.")	

def six(): 

    six=0
    print(f"AAA:")
    for item in list:
        if item.e >= 1900 and item.e <= 2000:
            six+=item.v
    print(f"AAAAA: {six} v.")
	
def asks():

    t=input("???: ")
    print(f"AAAAA {t} t pa: ")
    
    vanE = False
    for item in list:
        if t in item.t:
            print(item.n)
            vanE = True
    if not vanE:
            print("Not.")	


















