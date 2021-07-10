
mineOrd = []

def slaaSammen(t1,t2):
    sammen = t1 + " " + t2
    return sammen
# Test 1
#print(slaaSammen("Hei","Du"))


def skrivUt(liste):
    for ord in range(len(liste)):
        print(liste[ord])
#Test 2
#skrivUt(mineOrd)

def hovedprogram():
    t = input("Skriv et bokstav: ")

    while t != "stopp":
        if t == "i":
            txt1 = input("skriv ord 1 ")
            txt2 = input("Skriv ord 2 ")
            mineOrd.append(txt1)
            mineOrd.append(txt2)
            print(slaaSammen(txt1,txt2))
            t = input("Skriv et bokstav ")
        elif t =="u":
            skrivUt(mineOrd)
            t = input("Skriv et bokstav ")
        elif t == "s":
            exit()





print(hovedprogram())
