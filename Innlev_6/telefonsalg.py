def innlesning(filnavn):
    ansatt_dic = dict()
    lese_inn_fil = open(filnavn)
    for linje in lese_inn_fil:
# Splitter i forholdsvis key(navn) og val(salgstall)
# Key inneholder ord før " " - mellomrom
# Value inneholder ord etter " "
        (key, val) = linje.split()
        ansatt_dic[key] = int(val)
    return ansatt_dic


def maanedensSalgsperson(ordbok):
    maks = max(ordbok, key=ordbok.get)  # Just use 'min' instead of 'max' for minimum.
# vi sammenligner alle values in ordbok, ordbok.get gir oss values
    print(maks, ordbok[maks])

# Test 1
maanedensSalgsperson(innlesning("salgstall.txt"))


def totalAntallSalg(ordbok):
    sum = 0
    for linje in ordbok:
        sum += int(ordbok[linje])
    return sum

# Test 2
totalAntallSalg(innlesning("salgstall.txt"))

def gjennomsnittSalg(ordbok):
    snitt = round(totalAntallSalg(ordbok)/len(ordbok),2)
    return snitt

print(gjennomsnittSalg(innlesning("salgstall.txt")))


if __name__ == "__main__":
    def hovedprogram():
        print("Maanedens ansatte er: ")
        maanedensSalgsperson(innlesning("salgstall.txt"))
        print("Gjennomsnitlig salg denne maaneden:",gjennomsnittSalg(innlesning("salgstall.txt")) )
        print("Totalt antall salg: ", totalAntallSalg(innlesning("salgstall.txt")))

hovedprogram()