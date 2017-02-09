from CharGen.Rulesets.Pathfinder.Rules import *
from CharGen.Rulesets.Pathfinder import Spells

import random

class Adept:
    def __init__(self, level):
        self.level = level

        self.babTable = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
        self.badSaveTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.goodSaveTable = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.spellsPerDay = [
            [3, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 2, 1, 0, 0, 0, 0, 0, 0, 0],
            [3, 2, 1, 0, 0, 0, 0, 0, 0, 0],
            [3, 2, 1, 0, 0, 0, 0, 0, 0, 0],
            [3, 3, 2, 0, 0, 0, 0, 0, 0, 0],
            [3, 3, 2, 1, 0, 0, 0, 0, 0, 0],
            [3, 3, 2, 1, 0, 0, 0, 0, 0, 0],
            [3, 3, 2, 1, 0, 0, 0, 0, 0, 0],
            [3, 3, 3, 2, 0, 0, 0, 0, 0, 0],
            [3, 3, 3, 2, 1, 0, 0, 0, 0, 0],
            [3, 3, 3, 2, 1, 0, 0, 0, 0, 0],
            [3, 3, 3, 2, 1, 0, 0, 0, 0, 0],
            [3, 3, 3, 3, 2, 0, 0, 0, 0, 0],
            [3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
            [3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
            [3, 3, 3, 3, 2, 1, 0, 0, 0, 0],
            [3, 3, 3, 3, 2, 2, 0, 0, 0, 0],
            [3, 3, 3, 3, 2, 2, 0, 0, 0, 0]
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

        self.spellsKnown = []

    def randomize(self, character):
        # Pick some random spells the adept might prepare.
        allAdeptSpells = Spells.SpellList()
        allAdeptSpells.loadFromFile("CharGen/Rulesets/Pathfinder/Data/Spells/Adept.raw")

        # Pick our spells randomly
        spellsPerDay = self.getSpellsPerDay(character)
        spellLvl = 0
        for spellCount in spellsPerDay:
            # Pick spells.
            for i in range(1, spellCount):
                self.spellsKnown += [allAdeptSpells.getRandomSpell(spellLvl)]
            spellLvl += 1

    def getSpellsPerDay(self, character):
        spellsPerDay = self.spellsPerDay[self.level-1]

        # A character with a positive int mod might get extra spells slots.
        statMod = character.getStatMod("wis")
        if statMod > 0:
            extraSpellsPerDay = self.extraSpellsPerDay[statMod]
            for i in range(0, len(extraSpellsPerDay) - 1):
                if spellsPerDay[i] == 0:
                    extraSpellsPerDay[i] = 0

            spellsPerDay = [x + y for x, y in list(zip(spellsPerDay, extraSpellsPerDay))]

        # A wizard needs at least 10 + spell level int to cast a spell.
        int = character.getStat("wis")
        for i in range(0, len(spellsPerDay) - 1):
            if int < (10 + i):
                spellsPerDay[i] = 0

        return spellsPerDay

    def hd(self, character, total):
        return total + [(self.level, 6)]

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Adept"]

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
        #total["Craft ()"].classSkill = True
        total["Handle Animal"].classSkill = True
        total["Heal"].classSkill = True
        total["Knowledge (Arcana)"].classSkill = True
        total["Knowledge (Dungeoneering)"].classSkill = True
        total["Knowledge (Engineering)"].classSkill = True
        total["Knowledge (Geography)"].classSkill = True
        total["Knowledge (History)"].classSkill = True
        total["Knowledge (Local)"].classSkill = True
        total["Knowledge (Nature)"].classSkill = True
        total["Knowledge (Nobility)"].classSkill = True
        total["Knowledge (Planes)"].classSkill = True
        total["Knowledge (Religion)"].classSkill = True
        #total["Profession ()"].classSkill = True
        total["Spellcraft"].classSkill = True
        total["Survival"].classSkill = True

        return total

    def skillRanks(self, character, total):
        return total + 2 * self.level

    def weaponTraitProficiency(self, character, total):
        return total + ["Simple"]

    def spells(self, character, total):
        # Return with our spell list.
        adeptSpells = SpellList(self.level, "wis")
        for spell in self.spellsKnown:
            adeptSpells.addSpell(spell.name, spell.lvl)

        total["Adept Spells"] = adeptSpells
        return total
