#class Beispiel:
#    pass
#
#beispiel1=Beispiel()
#print(type(beispiel1))
#test
class Tier:
    spezies="Säugetier"
    def __init__(self, name, rasse, gefleckt=False ):
        self.name= name
        self.rasse=rasse
        self.gefleckt=gefleckt
    
    def wer_bin_ich(self):
        print("ich bin ein Tier")


class Hund(Tier):
    
    def __init__(self, name, rasse, gefleckt=False):
        Tier.__init__(self,name, rasse, gefleckt)
        print(f"hund {name} wurde angelegt")

    def wer_bin_ich(self):
        print("ich bin ein Hund")
        
    def bellen(self):
        print(f"{self.name} sagt: Wau! Wau!")
    
    def ball_holen(self):
        print(f"{self.name} hollt den ball")


class Katze(Tier):

    def __init__(self,name, rasse, gefleckt=False):
        Tier.__init__(self,name, rasse, gefleckt)
        print(f"katze {name} wurde angelegt")

    def wer_bin_ich(self):
        print("ich bin eine Katze")

    def miauen(self):
        print(f"{self.name} sagt Miau! Miau!")

    def klettern(self):
        print(f"{self.name} klettert den baum hoch")


nala=Katze(name="Nala", rasse="Kurzhaar")
print(nala.name)
print(nala.rasse)
print(nala.gefleckt)
print(nala.spezies)
nala.wer_bin_ich()

nala.miauen()
nala.klettern()



pongo=Hund(name="Pongo", rasse="Zwergpincher")
print(pongo.name)
print(pongo.rasse)
print(pongo.gefleckt)
pongo.wer_bin_ich()

rex=Hund(name="Rex", rasse="Schäferhund",gefleckt=True)
print(f"{rex.name} ist ein {rex.rasse} und ist gefleckt: {rex.gefleckt}")
rex.bellen()
rex.wer_bin_ich()

