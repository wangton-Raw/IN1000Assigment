# Oppgave 1
"""
tallrekke = [1,2,3]
print(tallrekke[0] + tallrekke[2])
"""
"""
navnlist = []
for a in range(4):
    navn = input("Skriv navnet her: ")
    navnlist.append(navn)
print(navnlist)

funnet = False
for names in range(len(navnlist)):
    if navnlist[names] == "Anton":
        funnet  = True

if funnet == True:
    print("Du husker meg! ")
else:
    print("Du glemte meg! ")
"""
"""
tallrekke1 = [1,2,3,4]
tallrekke2 = [3,4,5,6]
sumrekke = []

for index in range(len(tallrekke1)):
    sumrekke.append(tallrekke1[index]*tallrekke2[index])

print(sumrekke)
"""

# Oppgave 2 - Dictionary
produkter = {"melk":14.9, "brød":24.9,"yoghurt":12.9, "pizza":39.9}
"""
for pair in produkter.items():
    print(pair)

for a in range(2):
    vare =input("Skriv inn varen: ")
    pris = int(input ("Skiv inn prisen: "))
    produkter.update({vare:pris})
print(produkter)
"""

# Oppgave 4

bruker = input("Skriv inn navn på brukeren: ")
b_dict = {"Karen":"*frokost, lunsj, middag","Anna":"frokost,lunsj, middag"}

def listefunk(bruker):
    for key, value in b_dict.items():
        if key == bruker:
            return value
    return "Finnes ikke"

verdi = listefunk(bruker)
print(verdi)
