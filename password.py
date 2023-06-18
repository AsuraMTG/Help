
def eros_e_a_jelszo(jelszo):

    kisbetuk = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    nagybetuk = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']

    szamok = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    van_kisbetu = False
    van_nagybetu = False
    van_szam = False
    
    for kisbetu in kisbetuk:

        if kisbetu in jelszo:
            van_kisbetu = True

            break

    for nagybetu in nagybetuk:
        if nagybetu in jelszo:
            van_nagybetu = True
            break

    for szam in szamok:
        if str(szam) in jelszo:
            van_szam = True
            break

    eleg_hosszu = len(jelszo) >= 8

    return van_kisbetu and van_nagybetu and van_szam and eleg_hosszu


def jelszomegadas():

    jelszo = input("Kérlek, adj meg egy jelszót: ")

    while not eros_e_a_jelszo(jelszo):
        jelszo = input("A jelszó gyenge, adj meg újat: ")

    print("A jelszó elég erős , elmentettem...")

    with open("jelszo.txt", "w") as kimeneti_file:
        kimeneti_file.write(jelszo)


def egyezik(jelszo):
 
    try:
        with open("jelszo.txt") as bemeneti_file:
            helyes_jelszo = bemeneti_file.read()

    except:

        return

    helyes_jelszo = helyes_jelszo.strip()
    jelszo = jelszo.strip()

    return helyes_jelszo == jelszo


def beleptetes():
    
    probalkozasok = 3 

    megadott_jelszo = input("A belépéshez add meg a jelszót: ")
    probalkozas_szamlalo = 1

    while not egyezik(megadott_jelszo) and probalkozas_szamlalo < probalkozasok:        
        megadott_jelszo = input("A jelszó helytelen, kérlek, próbálkozz újra: ")
        probalkozas_szamlalo += 1

    if probalkozas_szamlalo >= probalkozasok:
        print("Túl sokszor próbálkoztál, sajnos egyik megadott jelszó sem volt helyes.")
        return False
    else:
        print("A jelszó helyes!")
        return True

if __name__ == "__main__":

    jelszomegadas()

    if beleptetes():
        print("Eljutottál a program védett részére!")
    
    else:
        print("Valószínűleg ellenséges kém vagy, nem játszhatsz a játékommal")
