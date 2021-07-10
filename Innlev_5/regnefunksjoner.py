
tall1 = -5
tall2 = 5
# En funksjon som adderer to tall
def adder(par1,par2):
    assert par1 and par2 <0
    sum = par1 + par2
    return sum
    
# Test 1
print(adder(tall1,tall2))

# En funksjon som subtraherer to tall
def subtrak(par1,par2):
    assert par1>0 or par2 >0
    sum = par2 - par1
    return sum
    
# Test 2
print(subtrak(tall1,tall2))

# En funksjons som dividerer to tall
def div(par1,par2):
    assert par1<0 and par2>0
    sum = par1/par2
    return sum
    
# Test 3
print(div(tall1,tall2))
"""
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    Cm = antallTommer * 2.54
    return Cm

def SkrivBeregninger():
    anntallCm = tommerTilCm(10)
    return anntallCm
print(SkrivBeregninger())

