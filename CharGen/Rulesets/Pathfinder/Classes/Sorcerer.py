from CharGen.Rulesets.Pathfinder.Rules import *

class Sorcerer:
    def __init__(self, level):
        self.level = level

    def hd(self, character, total):
        return total + [(self.level, 6)]

    def lvl(self, character, total):
        return total + self.level

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Sorcerer"]

    def spells(self, character, total):
        if not "Sorcerer Spells" in total.keys():
            total["Sorcerer Spells"] = SpellList(self.level, "int", "Spontaneous")

        spellList = total["Sorcerer Spells"]

        spellList.setSpellsPerDay(1, 3)
        spellList.setSpellsPerDay(2, 1)

        spellList.addSpell("Detect Magic", 0)
        spellList.addSpell("Read Magic", 0)
        spellList.addSpell("Color Spray", 1)
        spellList.addSpell("Sleep", 1)
        spellList.addSpell("Admonishing Ray", 2)
        spellList.addSpell("Admonishing Ray", 2)

        return total
