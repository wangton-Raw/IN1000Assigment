from random import randint
import random
from celle import Celle

class Spillebrett:
 def __init__(self, rader, kolonner):
     self.rader = int(rader)
     self.kolonner = int(kolonner)
     self.rutenett = []
     self.gen_nummer = 0
     self.gen_nummer +=1

     for rad in range(self.rader):
         self.rutenett.append([])
         print("")
         for kolon in range(self.kolonner):
             self._generer()
             self.rutenett[rad].append(Celle())
             self.tegnBrett()

 def tegnBrett(self):
     print(Celle.tegnRepresent(self), end="")

 def oppdatering(self):
    pass
 def finnAntallLevende(self):
    pass
 def _generer(self) :
    a = random.randint(0,2)
    # Hvis a == 2, så er cellen levende
    if a == 2:
        Celle.settLevende(self)

 def finnNabo(self, rad, kolonne):
    pass