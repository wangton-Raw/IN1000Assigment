import urllib.request

Url = "https://www.uio.no/studier/emner/matnat/ifi/IN1000/v20/obliger/temperatur.txt"
file = urllib.request.urlopen(Url)
# Leser URL og implementerer tallene fra fil txt til liste

def listeImp():
    templst = []
    for tall in file:
        templst.append(tall.decode('utf-8').strip())
    return templst

# Beregner gj.sntlig temperatur
def gjensnitt(liste):
    summer = 0
    for tall in range(len(liste)):
        summer += (int(liste[tall]))/len(liste)
    return summer

print(gjensnitt(listeImp()))



