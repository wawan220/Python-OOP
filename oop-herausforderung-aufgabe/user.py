


class Benutzer:
    def __init__(self, benutzername:str,passwort:str):
        self.__benutzername=benutzername
        self.__passwort=passwort

    def get_benutzername(self):
        pass

    def set_passwort(self,neuespasswort:str):
        pass

    def pruefe_login(self,passwort:str):
        pass

    def get_info(self):
        pass


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
