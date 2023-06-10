class Indian:
    def __init__(self, neve, neme, kora, tulajdona):
        
        self.neve = neve
        self.neme = neme
        self.kora = kora
        self.tulajdona = tulajdona

    
lista=[]

def beolvas():
    f=open("indian.txt", encoding="UTF-8")
    for sor in f:
        reszek=sor.strip().split(",")
        neve = reszek[0]
        neme = reszek[1]
        kora = int(reszek[2])
        tulajdona = reszek[3]
        obj = Indian(neve, neme, kora, tulajdona)
        lista.append(obj)
	
    f.close() 


def kiiratas():
    for item in lista:
        print(item.neve, item.neme, item.kora, item.tulajdona)

def f_3():

    print(f"\t3.f. A listában {len(lista)} fő indián szerepel.")

def f_4():

    halmaz=set([])
    for item in lista:
        halmaz.add(item.tulajdona)
    print(halmaz)

def f_5_6(): # értelmetlen ? mert másik fájlhoz készült!
    pass

def f_7():
    db=0
    for item in lista:
        if item.tulajdona == "tomahawk" and item.neme == "f":
            db+=1      
    print(f"\t7.f. {db} db férfinak van tomahawkja.")

def f_8_9_10(): # értelmetlen ? mert másik fájlhoz készült!
    pass


def main():
    beolvas()
    kiiratas()
    f_3()
    f_4()  #f_5_6 nem megoldható txt miatt!
    f_7()


main()    