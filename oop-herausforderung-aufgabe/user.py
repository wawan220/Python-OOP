


class Benutzer:
    def __init__(self, benutzername:str,passwort:str):
        self.__benutzername=benutzername
        self.__passwort=""   #wird durch den setter gesetzt (Validierung)
        self.set_passwort(passwort)

    def get_benutzername(self):
        return self.__benutzername

    def set_passwort(self,neues_passwort:str):
        if not isinstance(neues_passwort, str) or neues_passwort.strip()=="": #----> prüfe nach typ und inhalt darf nicht leer sein
            print("!!!FEHLER!!!")
            print("Passwort darf nicht leer sein!")
            return
        
        if len(neues_passwort) < 6:
            print("!!!Fehler!!!")
            print("Passwort muss mindestens 6 Zeichen lang sein!")
            return
        
        self.__passwort=neues_passwort
        print("Passwort wurde gesetzt/geändert!")

    def pruefe_login(self, passwort:str):
        if passwort == self.__passwort:
            return True
        return False

    def get_info(self):
        # Passwort aus sicherheitsgründen nicht anzeigen
        return(
            f"Typ: Benutzer\n"
            f"Benutzername: {self.__benutzername}"
        )


class Administrator(Benutzer):
    def __init__(self, benutzername:str, passwort:str, rechte_level:int):
        super().__init__(benutzername, passwort)
        self.__rechte_level=rechte_level

    def get_rechte_level(self):
        pass
    
    def set_rechte_level(self, neues_level:int):
        pass

    def get_info(self):
        pass


class Gastbenutzer(Benutzer):
    def __init__(self, benutzername:str, passwort:str, ablauf_tage:int):
        super().__init__(benutzername, passwort)
        self.__ablauf_tage=ablauf_tage

    def get_ablauf_tage(self):
        pass

    def set_ablauf_tage(self,tage:int):
        pass

    def pruefe_login(self,passwort:str):
        pass

    def get_info(self):
        pass
