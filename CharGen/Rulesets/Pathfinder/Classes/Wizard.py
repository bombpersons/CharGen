from CharGen.Rulesets.Pathfinder.Rules import *

class Wizard:
    def __init__(self, level):
        self.level = level

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Wizard"]

    def spells(self, character, total):
        if not "Wizard Spells" in total.keys():
            total["Wizard Spells"] = SpellList(self.level, "int", "Prepared")

        spellList = total["Wizard Spells"]

        spellList.addSpell("Detect Magic", 0)
        spellList.addSpell("Read Magic", 0)
        spellList.addSpell("Color Spray", 1)
        spellList.addSpell("Sleep", 1)
        spellList.addSpell("Admonishing Ray", 2)
        spellList.addSpell("Admonishing Ray", 2)

        return total
