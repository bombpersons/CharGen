import tkinter as tk

class CharacterGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Add main frame
        self.frame = CharacterFrame(self)
        # Set size
        self.geometry("1200x800+300+300")
        # Add a menu
        self.menu = CharacterMenu(self)

    def onExit(self):
        self.quit()

    def populate(self, character):
        self.menu.populate(character)
        self.frame.populate(character)

class CharacterMenu(object):
    def __init__(self, parent):
        self.parent = parent

    def populate(self, character):
        # Define menubar
        self.menubar = tk.Menu(self.parent.frame)
        self.parent.config(menu=self.menubar)

        # Define file menu options
        self.fileMenu = tk.Menu(self.parent.frame)
        self.menubar.add_cascade(label='File', menu=self.fileMenu)
        self.fileMenu.add_command(label='Exit', command=self.parent.onExit)

class CharacterFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def populate(self, character):
        self.parent.title("CharacterGUI")
        self.pack(fill=tk.BOTH, expand=True)

        frame1 = tk.Frame(self)
        frame1.pack(fill=tk.X)

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
            displayStat = tk.Label(frame1, text=statName+": "+str(statGetter()), width=50, anchor=tk.NW)
            displayStat.pack(side=tk.TOP, fill=tk.X, pady=5)
            self.labels.append(displayStat)
