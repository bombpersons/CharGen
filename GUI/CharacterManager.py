class CharacterManager:
    def __init__(self, t_characterType):
        self.characters = {}
        self.deletedCharacterIds = ()
        self.highestId = 0
        self.t_characterType = t_characterType

    def getCharacters(self):
        return self.characters

    def getFirstCharacter(self):
        if len(self.characters) > 0:
            return self.characters[next(iter(self.characters.keys()))]
        else:
            return None

    def getCharacter(self, id):
        return self.characters[id]

    def createCharacter(self):
        c = self.findFirstFreeCharacterId()
        self.characters[c] = self.t_characterType()
        return c

    def removeCharacter(self, id):
        if(id in self.characters.keys()):
            self.characters.remove(id)

    def findFirstFreeCharacterId(self):
        if len(self.deletedCharacterIds) > 0:
            c = self.deletedCharacterIds[0]
            del self.deletedCharacterIds[0]
        else:
            c = self.highestId
            self.highestId += 1

        return c
