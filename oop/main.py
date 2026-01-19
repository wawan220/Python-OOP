

class Player:
    def __init__(self, name:str,playerID: str):
        self.__name = name
        self.__playerID = playerID
    
    def getName(self):
        return self.__name

    def setName(self,name:str):
        self.__name=name

    def getPlayerID(self):
        return self.__playerID

    def setPlayerID(self,playerID:str):
        self.__playerID=playerID
    
    def __del__(self):
        print("deleted")



player1=Player(name="JoWi",playerID="ID1")
print(player1.getName())

player1.setName("PhMU")
print(player1.getName())

del(player1)
print(player1.getName())


