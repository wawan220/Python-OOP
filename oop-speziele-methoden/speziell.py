#Spezielle Methoden
#Magic / Dunder

liste=[1,2,3]
len(liste) #spezielle funktion

class Beispiel():
    pass

#beispiel=Beispiel()
#len(beispiel)

class Buch:
    def __init__(self,titel, autor, seiten):
        print("buch ist geschrieben")
        self.titel=titel
        self.autor=autor
        self.seiten=seiten
    
    def __del__(self):
        print("gelöscht")

    def __len__(self):
        return self.seiten    

    def __str__(self):  #-----> dunder für printausgaben
        return f"Titel: {self.titel} Autor: {self.autor} Seiten {self.seiten}"
        


buch=Buch("python rockt", "waldi", 1200)

print(buch)
print(len(buch))
del(buch)
del(buch)