import CharGen.Rulesets.Pathfinder.BaseTemplate as BaseTemplate

import CharGen.Rulesets.Pathfinder.Classes.Bard as Bard
import CharGen.Rulesets.Pathfinder.Classes.Commoner as Commoner

import CharGen.Rulesets.Pathfinder.Races.Dwarf as Dwarf
import CharGen.Rulesets.Pathfinder.Races.Goblin as Goblin

import CharGen.Rulesets.Pathfinder.Rules as Rules

def get():
	# Set up ruleset metadata
	metaData = {}
	
	# - Set up types
	metaData["Type"] = {}
	types = metaData["Type"]
	
	types["Character"] = Rules.PathfinderCharacter
	
	# - Set up templates
	metaData["Template"] = {}
	templates = metaData["Template"]
	
	# - - Set up base template
	templates["Base"] = BaseTemplate.BaseTemplate
	
	# - - Set up classes
	templates["Class"] = {}
	classes = templates["Class"]
	
	classes["Bard"] = Bard.Bard
	classes["Commoner"] = Commoner.Commoner
	
	# - - Set up races
	templates["Race"] = {}
	races = templates["Race"]
	
	races["Dwarf"] = Dwarf.Dwarf
	races["Goblin"] = Goblin.Goblin
	
	return metaData


if __name__ == "__main__":
	metaData = get()
	str(metaData)