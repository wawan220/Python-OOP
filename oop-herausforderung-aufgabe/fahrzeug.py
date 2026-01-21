

class Fahrzeug:
    def __init__(self, hersteller:str, modell:str,preis:float):
        self.__hersteller=hersteller
        self.__modell=modell
        self.__preis=preis

    def get_hersteller(self):
        pass

    def get_modell(self):
        pass
    
    def get_preis(self):
        pass

    def set_preis(self,neuerpreis:float):
        pass

    def berechne_gesamtpreis(self):
        pass

    def get_info(self):
        pass



class Auto(Fahrzeug):
    def __init__(self, hersteller, modell, preis, anzahl_tueren:int):
        super().__init__(hersteller, modell, preis)
        self.anzahl_tueren=anzahl_tueren

    def get_anzahl_tueren(self):
        pass
    
    def set_anzahl_tueren(self,neue_anz_tueren:int):
        pass

    def berechne_gesamtpreis(self):
        pass

    def get_info(self):
        pass


class Elektroauto(Auto):
    def __init__(self, hersteller, modell, preis, anzahl_tueren, batterie_kap:int):
        super().__init__(hersteller, modell, preis, anzahl_tueren)
        self.batterie_kap=batterie_kap

    def get_batterie_kap(self):
        pass
    
    def set_batterie_kap(self,neue_bat_kap:int):
        pass
    
    def berechne_gesamtpreis(self):
        pass

    def get_info(self):
        pass
