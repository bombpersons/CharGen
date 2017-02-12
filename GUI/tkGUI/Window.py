import tkinter as tk
import tkinter.ttk as ttk

import GUI.tkGUI.Rulesets.Pathfinder.CharacterWidget as CharacterWidget

class CharacterGUI(tk.Tk):
    def __init__(self, application, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Keep application reference
        self.app = application

        # Create character display list
        self.displayCharacters = ()

        # Add notebook
        self.characterTabs = {}
        self.characterNotebook = ttk.Notebook(self)
        self.characterNotebook.pack(fill=tk.BOTH, expand=tk.YES)
        self.setupNotebookFromApp()

        # Add main frame
        #self.frame = CharacterWidget.CharacterWidget(self)
        self.title("CharacterGUI")
        #self.pack(fill=tk.BOTH, expand=TRUE)
        # Set size
        self.geometry("%dx%d+%d+%d" % (1200, 800, 300, 300))
        # Add a menu
        self.menu = CharacterMenu(self, self.app)

    def setupNotebookFromApp(self):
        self.characterTabs = {}
        self.characterNotebook.destroy()
        self.characterNotebook = ttk.Notebook(self)
        characters = self.app.getCharacterManager().getCharacters()
        for k in characters.keys():
            newCharWidget = CharacterWidget.CharacterWidget(self, self.app, k)
            self.characterNotebook.add(newCharWidget, text="character")
            self.characterNotebook.select(newCharWidget)
            self.characterTabs[self.characterNotebook.select()] = newCharWidget
            print()

    def getSelectedCharacterTab(self):
         selectedCharacterTabId = self.characterNotebook.select()
         return self.characterTabs[selectedCharacterTabId]

    def commandNewCharacter(self):
        newCharacterId = self.app.getCharacterManager().createCharacter()
        newCharWidget = CharacterWidget.CharacterWidget(self, self.app, newCharacterId)
        self.characterNotebook.add(newCharWidget, text="character")
        self.characterNotebook.select(newCharWidget)
        self.characterTabs[self.characterNotebook.select()] = newCharWidget
        self.populate()

    def commandAddTemplate(self, t_template):
        selectedCharacterTab = self.getSelectedCharacterTab()
        selectedCharacter = selectedCharacterTab.getCharacter()
        selectedCharacter.apply(t_template())
        self.populate()

    def commandExit(self):
        self.quit()

    def populate(self):
        self.menu.populate()
        tabs = self.characterNotebook.tabs()
        for k, t in self.characterTabs.items():
            t.populate()

        self.characterNotebook.pack(fill=tk.BOTH, expand=tk.YES)

class CharacterMenu(object):
    def __init__(self, parent, application):
        self.parent = parent
        self.app = application

    def populate(self):
        # Define menubar
        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        # Define file menu options
        self.fileMenu = tk.Menu(self.parent)
        self.menubar.add_cascade(label='File', menu=self.fileMenu)
        self.fileMenu.add_command(label='New', command=self.parent.commandNewCharacter)
        self.fileMenu.add_command(label='Exit', command=self.parent.commandExit)

        # Define character menu options
        self.characterMenu = tk.Menu(self.parent)
        self.menubar.add_cascade(label='Character', menu=self.characterMenu)
        self.addTemplateMenu = tk.Menu(self.parent)
        self.characterMenu.add_cascade(label='Add Template', menu=self.addTemplateMenu)

        # Add templates
        # TODO: Ideally this should not be so hard-coded
        rules_metaData = self.app.getRules_metaData()
        t_baseTemplate = rules_metaData["Template"]["Base"]
        self.addTemplateMenu.add_command(label="Base Template", command=lambda parent=self.parent, t_template=t_baseTemplate: parent.commandAddTemplate(t_baseTemplate) )
