import GUI.CharacterManager as CharacterManager

class Application(object):
	def __init__(self, t_gui, rules_metaData):
		self.t_gui = t_gui
		self.rules_metaData = rules_metaData
		
		self.characterManager = CharacterManager.CharacterManager(self.getCharacterType())
		self.gui = t_gui(self)

	def getRules_metaData(self):
		return self.rules_metaData
		
	def getCharacterManager(self):
		return self.characterManager
		
	def getTypes(self):
		return self.rules_metaData["Type"]

	def getCharacterType(self):
		return self.getTypes()["Character"]

	def run(self):
		self.gui.populate()
		self.gui.mainloop()
