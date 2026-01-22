


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
    def __init__(self, ticket_id, beschreibung, status, wartungs_dauer:int):
        super().__init__(ticket_id, beschreibung, status)
        self.__wartungs_dauer=wartungs_dauer

    def get_wartungs_dauer(self):
        return self.__wartungs_dauer

    def set_wartungs_dauer(self, stunden:int):
        pass
    
    def set_status(self,neuer_status:str):      #-----> Status Überschreiben
        pass

    def get_info(self):
        pass
