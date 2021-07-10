# Oppgave 1

"""
navn = input("Skriv inn navn nr 1: ")
navn2 = input("Skriv inn navn nr 2: ")

print(" Hei " + navn +" " + navn2)

tall1 = 1
tall2 = 2

diff = tall1 - tall2
"""

# Oppgave 2
"""
spm = input("Vil du ha brus: ")

if spm == "ja":
    print("Her har du en brus!")
elif spm == "nei":
    print("Den er grei.")
else:
    print("Det forstod jeg ikke helt.")
"""
# Oppgave 3
from datetime import datetime

dagIN1 = int(input(" Angi dag: "))
månedIN1 = int(input (" Angi måned: "))
#dato = str(dagIN1) + "," + str(månedIN1) + "," + "20"
#konverter1 = datetime.strptime(dato,"%d,%m,%y")
#print(konverter1)

dagIN2 = int(input(" Angi dag nr 2: "))
månedIN2 = int(input (" Angi måned nr 2: "))
#dato2 = str(dagIN2) + "," + str(månedIN2) + "," + "20"
#konverter2 = datetime.strptime(dato,"%d,%m,%y")


rekke1 = månedIN1 + 0.1 * (dagIN1)
rekke2 = månedIN2 + 0.1 * (dagIN2)
if rekke1 == rekke2:
    print("Samme dato")
elif rekke1 < rekke2:
    print("riktig rekkefølge")