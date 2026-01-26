


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
        self.__rechte_level= 1          #wird durch den setter gesetzt (Validierung)
        self.set_rechte_level(rechte_level)

    def get_rechte_level(self):
        return self.__rechte_level
    
    def set_rechte_level(self, neues_level:int):
        if neues_level in (1,2,3,4,5):
            self.__rechte_level=neues_level
            print("Rechte-Level wurde gesetzt/geändert!")
        else:
            print("!!!Fehler!!!")
            print("Rechte-Level muss zwischen 1 und 5 liegen!")

    def get_info(self):
        return(
            f"Typ: Administrator\n"
            f"Benutzername: {self.get_benutzername()}"
            f"Rechte-Level: {self.__rechte_level}"
        )


class Gastbenutzer(Benutzer):
    def __init__(self, benutzername:str, passwort:str, ablauf_tage:int):
        super().__init__(benutzername, passwort)
        self.__ablauf_tage=1    #wird durch den setter gesetzt (Validierung)
        self.set_ablauf_tage(ablauf_tage)

    def get_ablauf_tage(self):
        return self.__ablauf_tage

    def set_ablauf_tage(self,tage:int):
        if tage > 0:
            self.__ablauf_tage=tage
            print("Ablauf-Tage wurden gesetzt/geändert")
        else:
            print("!!!Fehler!!!")
            print("Ablauf-Tage müssen größer 0 sein!")

    def pruefe_login(self,passwort:str):
        #Gast darf nur, wenn tage nicht abgelaufen!
        if self.__ablauf_tage <=0:
            return False
        # dannach nur mit passwortprüfung wie bei Benutzer
        return super().pruefe_login(passwort)

    def get_info(self):
        pass
