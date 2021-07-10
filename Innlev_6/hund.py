class Hund:
    def __init__(self, alder, vekt):
        self.alder = alder
        self.vekt = vekt
        self.metthet = 10


    def antallaar(self):
        return self.alder

    def veie(self):
        return self.vekt

    def spring(self):
        self.metthet -=1
        if self.metthet < 5:
            self.vekt -= 1

    def spis(self,heltall):
        self.metthet +=1
        if self.metthet > 7:
            self.vekt += heltall





