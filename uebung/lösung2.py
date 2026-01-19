import math
import random


def randomint():
    return random.randint(0,10)


class Zylinder:
    """Klasse Zylinder: initialisierung 
    mit hoehe und radius sowie Methoden 
    zur berechnung von Volumen und Oberfläche.
    """
    #pi= 3.14
    pi=math.pi

    def __init__(self, hoehe=1, radius=1):
        """Initialisierung des zylinders mit 
        hohe und radius
        """
        self.hoehe=hoehe
        self.radius=radius
               

    def volumen(self):
        """methode zur berechnung des Volumens."""
        return self.hoehe*self.pi*self.radius**2
        

    def oberflaeche(self):
        """methode zur berechnung der Oberflaeche"""
        top=self.pi*self.radius**2
        return 2*(top) + 2*self.pi*self.radius*self.hoehe



rand_hohe=randomint()
rand_radius=randomint()
print(rand_hohe,rand_radius)

zylinder1= Zylinder(2,3)
#print(zylinder1.volumen())      # ausgabe ---> 56.52
#print(zylinder1.oberflaeche())  # ausgabe ---> 94.2

zylinder2=Zylinder(hoehe=randomint(), radius=randomint())
zylinder3=Zylinder(hoehe=randomint(), radius=randomint())
zylinder4=Zylinder(hoehe=randomint(), radius=randomint())

print("zylinder 1")
print(zylinder1.volumen())      
print(zylinder1.oberflaeche())

print("zylinder 2")
print(zylinder2.volumen())      
print(zylinder2.oberflaeche())

print("zylinder 3")
print(zylinder3.volumen())      
print(zylinder3.oberflaeche())

print("zylinder 4")
print(zylinder4.volumen())      
print(zylinder4.oberflaeche())