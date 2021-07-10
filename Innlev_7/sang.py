class Sang:
    def __init__(self, tittel, artist):
        self.tittel = tittel.lower()
        self.artist = artist.lower()

    def __str__(self):
        return " Spiller " + self.tittel + " av " + self.artist

    def spill(self):
        melding = " Spiller " + self.tittel + " av " + self.artist
        print(melding)

    def sjekkArtist(self, navn):
        listeNavn = navn.split(" ")
        for ord in listeNavn:
            if self.artist.find(ord.lower(), 0, len(self.artist)) != -1:
                return True

        return False


    def sjekkTittel(self,tittel):
        return tittel.lower() == self.tittel

    def sjekkArtistogTittel(self,artist,tittel):
        return self.sjekkArtist(artist) and self.sjekkTittel(tittel)







