# del 1
def tellboks(skrivinn):
    tell = 0
    for letter in skrivinn:
        tell += 1
    return tell


# del 2
def tellord(setning):
    dic = dict()
    setningtab = setning.split()
    for i in setningtab:
        # 0 er value
        dic[i] = dic.get(i, 0) + 1
    return dic


if __name__ == "__main__":
    """"
    # test 1.
    skrivinn = "Hei"
    print("Det var " + str(tellboks(skrivinn)) + " bokstaver i ordet " + skrivinn)

    # test 2.
    setning = "Hei Hei på deg mann"
    setningtab = setning.split()
    dic = dict()
    print(tellord(setningtab))
    """

    # del 3
    sitat = "jeg liker kake , jeg ."
    Stabell = sitat.split()
    print("Det er totalt " + str(len(Stabell)) + " bokstaver ")
    print(tellord(sitat))
    for ord, value in tellord(sitat).items():
        print("Ordet {} forekommer {} og har {} bokstaver".format(ord,value, tellboks(ord)))




