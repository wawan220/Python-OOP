#liste = [1,2,3]
#
##liste.append()
#
#myset= set()
#print(type(myset))
#
#class Beispiel:
#    pass
#
##objekt anlegen
#objekt_klasse= Beispiel()
#print(type(objekt_klasse))
#

#beispiel atrebute:


class Hund:
    def __init__(self, meine_art, name, gefleckt):
        """mein Dok
        
        :param gefleckt boolean
        """
        self.art=meine_art
        self.name=name
        self.gefleckt=gefleckt

sam=Hund(meine_art="lab", name="sam",gefleckt=True)

print(sam.name)
print(sam.gefleckt)



#bello=Hund(meine_art="Pudel")
#charly= Hund(meine_art="Huskie")

#print(bello.art)
#print(charly.art)