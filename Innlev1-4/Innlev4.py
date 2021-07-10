# Oppgave 1

"""
def adder(tall1,tall2):
    produkt = tall1 + tall2
    return produkt

print(adder(4,2))
print(adder(1,5))
"""

# Skal be brukeren skrive et ord, så skal programmet
# finne ut hvor mange "e" det er i ordet, feks.
"""
skrivinn = input("Skriv ordet her: ")
skrivboks = input("Skriv inn bokstaven: ")

def sjekk(skrivinn,skrivboks):
    count = 0
    for letter in skrivinn:
        if letter == skrivboks:
            count += 1
    return "Det var " + str(count)+ " " + skrivboks + " i ordet " + skrivinn

print(sjekk(skrivinn,skrivboks))
"""

# Oppgave 2
"""
i = 0
minsum = 0
taste = input("tast inn et nummer: ")
liste = []
while int(taste) != 0:
    liste.append(taste)
    print(liste)
    taste = input("tast inn et nummer: ")

while i < len(liste):
    print(liste[i])
    minsum = minsum + int(liste[i])
    i +=1
print(minsum)

minst = 0
for a in range(len(liste)):
   minst = min(liste)
print("Minste tallet er " + minst)

for a in range(len(liste)):
    storst = max(liste)
print("Største tallet er " + storst)
"""

# Oppgave 4
"""
reisemaal = ["Norge","Sverige","DAM","KAL","MAL"]

for a in range(5):
    inn = input("Skriv inn 5 reisemål:")
    reisemaal.append(inn)

print(reisemaal)
klesplagg = ["GENSER","SKJORTE","T-SHORTE","ØRER","DAPPER"]
avreisedato = [20.08, 20.09, 20.10, 20.11, 20.12]

for a in range(5):
    innK = input("Skriv inn klesplagg: ")
    innA = input("Skriv inn avreisedato: ")
    klesplagg.append(innK)
    avreisedato.append(innA)
print(klesplagg)
print(avreisedato)

reiseplan =[reisemaal,klesplagg,avreisedato]

#print(reiseplan)

for a in range(len(reiseplan)):
    print(reiseplan[a])

I1 = int(input("Skriv inn nummer: "))
I2 = int(input("Skriv inn nummer: "))

if 0 <= int(I1)<= len(reiseplan) and 0<= int(I2)<= len(reiseplan[0]):
    print(reiseplan[I1][2])
else:
    print("Ugyldig input")
"""

# Oppgave 5
"""
skrivinn = "Hei"


def tellboks(skrivinn):
  tell = 0
  for letter in skrivinn:
    tell +=1
  return tell

print("Det var "+  str(tellboks(skrivinn)) + " bokstaver i ordet " + skrivinn )

# Hvert ord er keyname
setning = "Hei Hei på deg mann"
setningtab = setning.split()
dic = dict()
def tellord(setningtab):
  for i in setningtab:
# 0 er value
    dic[i] = dic.get(i,0) + 1
  return dic
print(tellord(setningtab))
"""

ordet = "hei hei på deg mann"
ordlst = ordet.split()
orddic = {}

def kombo(ordlst):
  tell = 0
  lst = []
  talllst = []
  for x in ordlst:
    orddic[x] = orddic.get(x,0) + 1
  lst = list(orddic.keys())
  print(lst)

  for y in orddic:
    print("Ordet {} forekommer {}".format(y,orddic[y]))

kombo(ordlst)





"""""
for a in range(len(orddic)):
  print([key for key in orddic.keys()][a])

"""""
