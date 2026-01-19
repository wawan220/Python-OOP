class Linie:
    """ Klasse Linie: Initialisierung mit zwie Koordinaten und
        methoden zur berechnung von Distanz und Steigung.
    """

    def __init__(self, koor1, koor2):
        """Initialisierung mit den zwei Koordinaten koor1 und koor2."""
        self.koor1=koor1
        self.koor2=koor2
        

    def distanz(self):
        """methode zur Berechnung der Distanz der beiden koordinaten."""
        x1, y1 =self.koor1
        x2, y2=self.koor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
        

    def steigung(self):
        """Methode zur Berechnung der steigerung zwischen beiden koordinaten"""
        x1, y1=self.koor1
        x2, y2=self.koor2
        return (y2-y1)/(x2-x1)


koordinate1 =(3,2)
koordinate2 = (8,10)

linie = Linie(koordinate1, koordinate2)

print(f"distanz {linie.distanz()}")
    # Ausgabe: 9.34339.... 

print(f"steigung {linie.steigung()}")
    # Ausgabe: 1.6
