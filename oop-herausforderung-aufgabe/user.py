


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
            f"Benutzername: {self.get_benutzername()}\n"
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
        return(
            f"Typ: Gast-Benutzer\n"
            f"Benutzername: {self.get_benutzername()}\n"
            f"Ablauf-Tage: {self.__ablauf_tage}"
        )


#=========TEST===============

user1=Benutzer(benutzername="max", passwort="geheim123")
user1.set_passwort(neues_passwort="streng-geheim123")
user1.set_passwort(neues_passwort="12345")
user1.set_passwort(neues_passwort="")
print(user1.get_info())

admin1=Administrator(benutzername="admin",passwort="admin123",rechte_level=3)
admin1.set_rechte_level(10)
admin1.set_rechte_level(3)

print(admin1.get_info())

gast1=Gastbenutzer(benutzername="guest",passwort="guest123",ablauf_tage=3)
print(gast1.get_info())


print("user login richtig: ",user1.pruefe_login("streng-geheim123"))
print("user login falsch: ",user1.pruefe_login("streng-geheim12"))


print("gast richtig: ", gast1.pruefe_login("guest123"))
print("gast Falsch: ", gast1.pruefe_login("guest12"))

gast1.set_ablauf_tage(1)
print("gast login (1tag): ", gast1.pruefe_login("guest123"))

gast1._Gastbenutzer__ablauf_tage =0
print("gast login (0tag): ", gast1.pruefe_login("guest123"))