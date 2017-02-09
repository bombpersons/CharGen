from CharGen.Rulesets.Pathfinder.Rules import *
from CharGen.Rulesets.Pathfinder import Spells

import random

# Our version of sorcerer is also gimped a little.
# Generating the bloodlines and all that crap is too complicated,
# so we'll just be giving them a bunch of spells.

class Sorcerer:
    def __init__(self, level):
        self.level = level

        self.babTable = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
        self.badSaveTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.goodSaveTable = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.spellsPerDay = [
            [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 6, 3, 0, 0, 0, 0, 0, 0, 0],
            [0, 6, 4, 0, 0, 0, 0, 0, 0, 0],
            [0, 6, 5, 3, 0, 0, 0, 0, 0, 0],
            [0, 6, 6, 4, 0, 0, 0, 0, 0, 0],
            [0, 6, 6, 5, 3, 0, 0, 0, 0, 0],
            [0, 6, 6, 6, 4, 0, 0, 0, 0, 0],
            [0, 6, 6, 6, 5, 3, 0, 0, 0, 0],
            [0, 6, 6, 6, 6, 4, 0, 0, 0, 0],
            [0, 6, 6, 6, 6, 5, 3, 0, 0, 0],
            [0, 6, 6, 6, 6, 6, 4, 0, 0, 0],
            [0, 6, 6, 6, 6, 6, 5, 3, 0, 0],
            [0, 6, 6, 6, 6, 6, 6, 4, 0, 0],
            [0, 6, 6, 6, 6, 6, 6, 5, 3, 0],
            [0, 6, 6, 6, 6, 6, 6, 6, 4, 0],
            [0, 6, 6, 6, 6, 6, 6, 6, 5, 3],
            [0, 6, 6, 6, 6, 6, 6, 6, 6, 4],
            [0, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        ]
        self.spellsKnown = [
            [4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 3, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 3, 1, 0, 0, 0, 0, 0, 0, 0],
            [6, 4, 2, 0, 0, 0, 0, 0, 0, 0],
            [7, 4, 2, 1, 0, 0, 0, 0, 0, 0],
            [7, 5, 3, 2, 0, 0, 0, 0, 0, 0],
            [8, 5, 3, 2, 1, 0, 0, 0, 0, 0],
            [8, 5, 4, 3, 2, 0, 0, 0, 0, 0],
            [9, 5, 4, 3, 2, 1, 0, 0, 0, 0],
            [9, 5, 5, 4, 3, 2, 0, 0, 0, 0],
            [9, 5, 5, 4, 3, 2, 1, 0, 0, 0],
            [9, 5, 5, 4, 4, 3, 2, 0, 0, 0],
            [9, 5, 5, 4, 4, 3, 2, 1, 0, 0],
            [9, 5, 5, 4, 4, 4, 3, 2, 0, 0],
            [9, 5, 5, 4, 4, 4, 3, 2, 1, 0],
            [9, 5, 5, 4, 4, 4, 3, 3, 2, 0],
            [9, 5, 5, 4, 4, 4, 3, 3, 2, 1],
            [9, 5, 5, 4, 4, 4, 3, 3, 3, 2],
            [9, 5, 5, 4, 4, 4, 3, 3, 3, 3]
        ]
        self.extraSpellsPerDay = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 2, 2, 1, 1, 1, 1, 0, 0, 0],
            [0, 2, 2, 2, 1, 1, 1, 1, 0, 0],
            [0, 2, 2, 2, 2, 1, 1, 1, 1, 0],
            [0, 3, 2, 2, 2, 2, 1, 1, 1, 1],
            [0, 3, 3, 2, 2, 2, 2, 1, 1, 1],
            [0, 3, 3, 3, 2, 2, 2, 2, 1, 1],
            [0, 3, 3, 3, 3, 2, 2, 2, 2, 1],
            [0, 4, 3, 3, 3, 3, 2, 2, 2, 2],
            [0, 4, 4, 3, 3, 3, 3, 2, 2, 2],
            [0, 4, 4, 4, 3, 3, 3, 3, 2, 2],
            [0, 4, 4, 4, 4, 3, 3, 3, 3, 2],
            [0, 5, 4, 4, 4, 4, 3, 3, 3, 3]
        ]

        self.spellsLearnt = []

    def randomize(self, character):
        # Pick some random spells the wizard might know.
        allWizardSpells = Spells.SpellList()
        allWizardSpells.loadFromFile("CharGen/Rulesets/Pathfinder/Data/Spells/Wizard.raw")

        # Pick our spells randomly
        spellsKnown = self.getSpellsKnown(character)
        spellLvl = 0
        for spellCount in spellsKnown:
            # Pick spells.
            for i in range(1, spellCount):
                self.spellsLearnt += [allWizardSpells.getRandomSpell(spellLvl)]
            spellLvl += 1

    def getSpellsKnown(self, character):
        spellsKnown = self.spellsKnown[self.level-1]

        # A wizard needs at least 10 + spell level int to cast a spell.
        stat = character.getStat("cha")
        for i in range(0, len(spellsKnown) - 1):
            if stat < (10 + i):
                spellsKnown[i] = 0

        return spellsKnown

    def getSpellsPerDay(self, character):
        spellsPerDay = self.spellsPerDay[self.level-1]

        # A character with a positive int mod might get extra spells slots.
        statMod = character.getStatMod("cha")
        if statMod > 0:
            extraSpellsPerDay = self.extraSpellsPerDay[statMod]
            for i in range(0, len(extraSpellsPerDay) - 1):
                if spellsPerDay[i] == 0:
                    extraSpellsPerDay[i] = 0

            spellsPerDay = [x + y for x, y in list(zip(spellsPerDay, extraSpellsPerDay))]

        return spellsPerDay

    def hd(self, character, total):
        return total + [(self.level, 6)]

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Sorcerer"]

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

    def weaponTraitProficiency(self, character, total):
        total += ["Simple"]
        return total

    def spells(self, character, total):
        # Return with our spell list.
        spells = SpellList(self.level, "cha")
        for spell in self.spellsLearnt:
            spells.addSpell(spell.name, spell.lvl)

        # Set how many times we can cast.
        spellsPerDay = self.getSpellsPerDay(character)

        i = 0
        for spellCount in spellsPerDay:
            spells.setSpellsPerDay(i, spellCount)
            i += 1

        total["Sorcerer Spells"] = spells
        return total
