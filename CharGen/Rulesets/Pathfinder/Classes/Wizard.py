from CharGen.Rulesets.Pathfinder.Rules import *
from CharGen.Rulesets.Pathfinder import Spells

import random

class Wizard:
    def __init__(self, level):
        self.level = level

        self.babTable = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
        self.badSaveTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.goodSaveTable = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.spellsPerDay = [
            [3, 1],
            [4, 2],
            [4, 3, 1],
            [4, 3, 2],
            [4, 3, 2, 1],
            [4, 3, 3, 2],
            [4, 4, 3, 2, 1],
            [4, 4, 3, 3, 2],
            [4, 4, 4, 3, 2, 1],
            [4, 4 ,4, 3, 3, 2],
            [4, 4, 4, 4, 2, 1],

        ]

    def hd(self, character, total):
        return total + [(self.level, 6)]

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Wizard"]

    def lvl(self, character, total):
        return total + self.level

    def BAB(self, character, total):
        return total + self.babTable[self.level]

    def fortSaveBonus(self, character, total):
        return total + self.badSaveTable[self.level]
    def refSaveBonus(self, character, total):
        return total + self.badSaveTable[self.level]
    def willSaveBonus(self, character, total):
        return total + self.goodSaveTable[self.level]

    def skills(self, character, total):
        total["Appraise"].classSkill = True
        #total["Craft ()"].classSkill = True
        total["Fly"].classSkill = True
        total["Linguistics"].classSkill = True
        #total["Profession ()"].classSkill = True
        total["Spellcraft"].classSkill = True

        return total

    def skillRanks(self, character, total):
        return total + 2 * self.level

class WizardRandom(Wizard):
    def __init__(self, level):
        Wizard.__init__(self, level)

        # Pick some random spells the wizard might know.
        wizardSpells = Spells.SpellList()
        wizardSpells.loadFromFile("CharGen/Rulesets/Pathfinder/Data/Spells/Wizard.raw")

        self.spellsKnown = []
        self.spellsKnown += [wizardSpells.getRandomSpellByLvl(1)]
        self.spellsKnown += [wizardSpells.getRandomSpellByLvl(2)]

    def spells(self, character, total):
        wizardSpells = SpellList(self.level, "int")
        for spell in self.spellsKnown:
            wizardSpells.addSpell(spell.name, spell.lvl)

        total["Wizard Spells"] = wizardSpells
        return total
