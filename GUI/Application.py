class Application(object):
	def __init__(self, t_gui, t_character):
		self.t_gui = t_gui
		self.t_character = t_character
		
		self.gui = t_gui()
		self.character = t_character()
		
	def run(self):
		self.gui.populate(self.character)
		self.gui.mainloop()