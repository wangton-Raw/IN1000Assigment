class Celle:
 # Konstruktør
 def __init__(self):
  self.status = "død"

 # Endre status
 def settDoed(self):
  self.status = "død"

 def settLevende(self):
  self.status = "levende"

 # Hente status
 def erLevende(self):
  if self.status == "levende":
   return True
  else:
   return False

 def tegnRepresent(self):
  if self.status == "levende":
   return "0"
  else:
   return "."

 def hentStatusTegn(self):
  pass