from hund import Hund

def hovedprogram():
    hund1 = Hund(2,20)
    hund1.spring()
    hund1.spring()
    hund1.spis(1)
    hund1.spis(1)


from datetime import datetime
now = datetime.now()

print ('%02d-%02d-%04d' % (now.month, now.day, now.year))
print ('%02d:%02d:%04d' % (now.hour, now.minute, now.second))

print ('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year,now.hour, now.minute, now.second))


print (f'{now.month:>02}-{now.day}-{now.year}' )

import re

hei = input("Please provide some info: ")
""""
if not re.match("^[s and m or S and M]*$", hei):
    print ("Error! Only letters a-z allowed!")
    exit()
else:
    print("jada")
"""
while not re.match("^[a-zA-Z]*$", hei):
    hei = input(("Skriv en bokstav da!: " ))