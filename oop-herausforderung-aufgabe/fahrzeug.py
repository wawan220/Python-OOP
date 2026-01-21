

class Fahrzeug:
    def __init__(self, hersteller:str, modell:str,preis:float):
        self.__hersteller=hersteller
        self.__modell=modell
        self.__preis=preis

    #---------- GETTER --------------
    def get_hersteller(self):
        return self.__hersteller

    def get_modell(self):
        return self.__modell
    
    def get_preis(self):
        return self.__preis

    #---------- SETTER --------------
    def set_preis(self,neuerpreis:float):
        if neuerpreis>0:
            self.__preis = neuerpreis
            print("Preis wurde geändert")
        else:
            print("!!! FEHLER !!!")
            print("Preis muss Grösser als null sein")

    #---------- Methoden --------------
    def berechne_gesamtpreis(self):
        return self.get_preis()

    def get_info(self):
        return(
            f"Hersteller: {self.__hersteller}\n"
            f"Modell: {self.__modell}\n"
            f"Preis: {self.__preis:.2f}€"
        )



class Auto(Fahrzeug):
    def __init__(self, hersteller, modell, preis, anzahl_tueren:int):
        super().__init__(hersteller, modell, preis)
        self.__anzahl_tueren=anzahl_tueren

    def get_anzahl_tueren(self):
        return self.__anzahl_tueren
        
    
    def set_anzahl_tueren(self,neue_anz_tueren:int):
        if neue_anz_tueren in (1,2,3,4,5):
            self.__anzahl_tueren=neue_anz_tueren
            print("Preis wurde geändert")
        else:
            print("!!!Fehler!!!")
            print("Ungültige anzahl der Tueren")


    def berechne_gesamtpreis(self):
        #Auto 10% Aufschlag
        return self.get_preis()*1.10

    def get_info(self):
        return(
            super().get_info()
            + f"\nTüren: {self.__anzahl_tueren}"
            + f"\nGesamtpreis: {self.berechne_gesamtpreis():.2f}€"
        )


class Elektroauto(Auto):
    def __init__(self, hersteller, modell, preis, anzahl_tueren, batterie_kap:int):
        super().__init__(hersteller, modell, preis, anzahl_tueren)
        self.__batterie_kap=batterie_kap

    def get_batterie_kap(self):
        return self.__batterie_kap
    
    def set_batterie_kap(self,neue_bat_kap:int):
        if neue_bat_kap>0:
            self.__batterie_kap=neue_bat_kap
            print("Batteriekapazitaet geändert")
        else:
            print("!!!Fehler!!!")
            print("Bateriekapazitaet muss groesser null sein")
    
    def berechne_gesamtpreis(self):
        #Auto 10% Aufschlag minus 2000 Euro
        return (self.get_preis()*1.10)-2000
        
    def get_info(self):
        return(
            super().get_info()
            + f"\nBatteriekap: {self.__batterie_kap} kwh"
        )




fahrzeug1=Fahrzeug(hersteller="VW",modell="Basis",preis=20000)
auto1=Auto(hersteller="VW",modell="Golf",preis=25000,anzahl_tueren=5)
elektro1=Elektroauto(hersteller="Tesla",modell="Model 3",preis=42000,anzahl_tueren=5, batterie_kap=60)


fahrzeug1.set_preis(neuerpreis=21000)
auto1.set_preis(30000)
elektro1.set_batterie_kap(80)
elektro1.set_preis(35000)

print(fahrzeug1.get_info())
print("------------------------")
print(auto1.get_info())
print("------------------------")
print(elektro1.get_info())