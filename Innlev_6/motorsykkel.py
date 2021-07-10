class Motorsykkel:
    def __init__(self,merke, registerNr, kilometer):
        self.merke = merke
        self.registerNr = registerNr
        self.kilometer = kilometer

    def kjor(self,km):
        self.kilometer = self.kilometer + km

    def hentKilometerstand(self):
        return self.kilometer

    def SkrivUt(self):
        print(self.merke)
        print(self.registerNr)
        print(self.kilometer)



