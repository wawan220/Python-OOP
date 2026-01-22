


class Ticket:
    #---------------- ATRIBUTE ---------------------
    def __init__(self, ticket_id:int, beschreibung:str, status:str="offen"):
        self.__ticket_id=ticket_id
        self.__beschreibung=beschreibung
        self.__status="offen"
        self.set_status(status)

    #---------------- METHODEN ---------------------
    def get_ticket_id(self):
        return self.__ticket_id
    
    def get_beschreibung(self):
        return self.__beschreibung

    def get_status(self):
        return self.__status

    def set_status(self,neuer_status:str):
        erlaubter_status = ("offen","in_bearbeitung","geschlossen")
        if neuer_status in erlaubter_status:
            self.__status=neuer_status
            print(f"Status geändert auf: {neuer_status}")
        else:
            print("!!!FEHLER!!")
            print("Ungültige Status! erlaubt: \n > offen, in_bearbeitung, geschlossen")

    def get_info(self):
        return (
            f"Typ: Ticket \n"
            f"ID: {self.__ticket_id} \n"
            f"Beschreibung: {self.__beschreibung} \n"
            f"Status: {self.__status}"   
        )


class PrioritaetsTicket(Ticket):
    def __init__(self, ticket_id, beschreibung, status, prioritaet:int=3):
        super().__init__(ticket_id, beschreibung, status)
        self.__prioritaet=3
        self.set_prioritaet(prioritaet)
    
    def get_prioritaet(self):
        return self.__prioritaet

    def set_prioritaet(self,neue_prioritaet:int):
        erlaubter_prio = (1,2,3,4,5)
        if neue_prioritaet in erlaubter_prio:
            self.__prioritaet=neue_prioritaet
            print(f"Priorität geändert auf: {neue_prioritaet}")
        else:
            print("!!!FEHLER!!")
            print("Ungültige Priorität! erlaubt: \n > 1,2,3,4,5")

    def get_info(self):
        return (
            f"Typ: PrioritaetsTicket \n"
            f"ID: {self.get_ticket_id()} \n"
            f"Beschreibung: {self.get_beschreibung()} \n"
            f"Status: {self.get_status()}" 
            f"Priorität: {self.__prioritaet}"  
        )


class WartungsTicket(Ticket):
    def __init__(self, ticket_id, beschreibung, status, wartungs_dauer:int=1):
        super().__init__(ticket_id, beschreibung, status)
        self.__wartungs_dauer=1
        self.__in_bearbeitung=False   #internes Atribut / als Merkhilfe
        self.set_wartungs_dauer(wartungs_dauer)

    def get_wartungs_dauer(self):
        return self.__wartungs_dauer

    def set_wartungs_dauer(self, stunden:int):
        if stunden>0:
            self.__wartungs_dauer = stunden
            print(f"Wartungsdauer geänder auf {stunden} Stunden")
        else:
            print("!!!FEHLER!!")
            print("Ungültige Wartungsdauer! muss grösser als 0 sein:")
    
    def set_status(self,neuer_status:str):      #-----> Status Überschreiben
        erlaubter_status = ("offen","in_bearbeitung","geschlossen")
        #Prüfung nach inhalt
        if neuer_status not in erlaubter_status:
            print("!!!FEHLER!!")
            print("Ungültige Status! erlaubt: \n > offen, in_bearbeitung, geschlossen")
            return
        
        #Regel1: nicht direkt auf geschlossen setzen --> ersmal in_bearbeitung
        if neuer_status =="geschlossen" and not self.__in_bearbeitung:
            print("!!!FEHLER!!")
            print("Wartungsticket darf nicht direkt geschlossen werden")
            print("Wartungsticket muss erst in_bearbeitung gesetzt werden")
            return
        
        if neuer_status=="in_bearbeitung":
            self.__in_bearbeitung=True
            print(f"Status geänder in: > {neuer_status}")

        #Marker setzen in Bassisklasse / Elternklasse 
        super().set_status(neuer_status)
        print(f"Status geänder auf: {neuer_status}")

    def get_info(self):
        return (
            f"Typ: WartungsTicket \n"
            f"ID: {self.get_ticket_id()} \n"
            f"Beschreibung: {self.get_beschreibung()} \n"
            f"Status: {self.get_status()}" 
            f"Wartungsdauer: {self.__wartungs_dauer} Stunden"  
        )








# ---------------- TESTPROGRAMM ----------------
if __name__ == "__main__":
    print("=== OBJEKTE ERZEUGEN ===")
    t1 = Ticket(1, "Drucker druckt nicht", "offen")
    p1 = PrioritaetsTicket(2, "Server down", "offen", 5)
    w1 = WartungsTicket(3, "Patchday Wartung", "offen", 4)

    print("\n=== INFOS ===")
    print(t1.get_info())
    print("------------------------")
    print(p1.get_info())
    print("------------------------")
    print(w1.get_info())

    print("\n=== STATUS-TESTS (gültig/ungültig) ===")
    t1.set_status("in_bearbeitung")
    t1.set_status("geschlossen")
    t1.set_status("irgendwas")  # ungültig

    print("\n=== PRIORITÄT-TESTS ===")
    p1.set_prioritaet(2)
    p1.set_prioritaet(9)  # ungültig

    print("\n=== WARTUNGSTICKET-REGEL TEST ===")
    # darf NICHT direkt geschlossen werden
    w1.set_status("geschlossen")  # soll Fehler bringen
    w1.set_status("in_bearbeitung")  # ok
    w1.set_status("geschlossen")  # jetzt ok

    print("\n=== WARTUNGSDAUER-TESTS ===")
    w1.set_wartungs_dauer(0)  # ungültig
    w1.set_wartungs_dauer(6)  # gültig

    print("\n=== FINAL INFOS ===")
    print(t1.get_info())
    print("------------------------")
    print(p1.get_info())
    print("------------------------")
    print(w1.get_info())
