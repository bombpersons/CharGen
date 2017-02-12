import tkinter as tk

class CharacterWidget(tk.Frame):
    def __init__(self, parent, application, characterId):
        tk.Frame.__init__(self, parent)
        self.app = application
        self.characterId = characterId
        self.innerFrame = None

    def getCharacterId(self):
        return self.characterId

    def getCharacter(self):
        return self.app.getCharacterManager().getCharacter(self.characterId)

    def populate(self):
        #self.pack(fill=tk.BOTH, expand=True)

        character = self.getCharacter()

        if self.innerFrame != None:
            self.innerFrame.destroy()
        self.innerFrame = tk.Frame(self)
        self.innerFrame.pack(fill=tk.X)

        self.labels = []

        displayList = (
            ("Name",character.getName),
            ("Speed",character.getSpeed),
            ("AC",character.getAC),
            ("Touch AC",character.getTouchAC),
            ("FF AC",character.getFlatAC),
            ("Fortitude Save",character.getFortSave),
            ("Reflex Save",character.getRefSave),
            ("Will Save",character.getWillSave),
            ("CMD",character.getCMD),
            ("CMB",character.getCMB),
            ("BAB",character.getBAB)
        )

        for statName,statGetter in displayList:
            displayStat = tk.Label(self.innerFrame, text=statName+": "+str(statGetter()), width=50, anchor=tk.NW)
            displayStat.pack(side=tk.TOP, fill=tk.X, pady=5)
            self.labels.append(displayStat)
