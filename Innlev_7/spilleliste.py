from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self,filnavn):
        lesfil = open(filnavn)
        for linje in lesfil:
            formatering = linje.strip().split(";")
            self._sanger.append(Sang(formatering[0], formatering[1]))

    def leggTilSang(self,nySang):
        self._sanger.append(nySang)

    def fjernSang(self,sang):
        self._sanger.remove(sang)

    def spillSang(self,sang):
        print(sang)

    def spillAlle(self):
        for sang in self._sanger:
            print(sang)

    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang
        return None

    def hentArtistUtvalg(self, artistnavn):
        listeUtvalg = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                listeUtvalg.append(sang)
        return listeUtvalg
