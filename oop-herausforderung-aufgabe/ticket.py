


class Ticket:
    #---------------- ATRIBUTE ---------------------
    def __init__(self, ticket_id:int, beschreibung:str, status:str):
        self.__ticket_id=ticket_id
        self.__beschreibung=beschreibung
        self.__status=status

    #---------------- METHODEN ---------------------
    def get_ticket_id(self):
        pass
    
    def get_beschreibung(self):
        pass

    def get_status(self):
        pass

    def set_status(self,neuer_status:str):
        self.__status = neuer_status

    def get_info(self):
        pass


class PrioritaetsTicket(Ticket):
    def __init__(self, ticket_id, beschreibung, status, prioritaet:int):
        super().__init__(ticket_id, beschreibung, status)
        self.__prioritaet=prioritaet
    
    def get_prioritaet(self):
        pass

    def set_prioritaet(self,neue_prioritaet:int):
        pass

    def get_info(self):
        pass


class WartungsTicket(Ticket):
    def __init__(self, ticket_id, beschreibung, status, wartungs_dauer:int):
        super().__init__(ticket_id, beschreibung, status)
        self.__wartungs_dauer=wartungs_dauer

    def get_wartungs_dauer(self):
        pass

    def set_wartungs_dauer(self, stunden:int):
        pass
    
    def set_status(self,neuer_status:str):      #-----> Status Überschreiben
        pass

    def get_info(self):
        pass
