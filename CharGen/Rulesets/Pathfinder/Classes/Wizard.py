from CharGen.Rulesets.Pathfinder.Rules import *
from CharGen.Rulesets.Pathfinder import Spells

import random

# So our version of the pathfinder wizard is kinda gimped,
# since it doesn't have any of the abilities the school specialization gives you
# plus they can't have familiars.

# Makes it much easier to randomly generate though.

class Wizard:
    def __init__(self, level):
        self.level = level

        self.babTable = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
        self.badSaveTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.goodSaveTable = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.spellsKnown = [
            [3, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 3, 1, 0, 0, 0, 0, 0, 0, 0],
            [4, 3, 2, 0, 0, 0, 0, 0, 0, 0],
            [4, 3, 2, 1, 0, 0, 0, 0, 0, 0],
            [4, 3, 3, 2, 0, 0, 0, 0, 0, 0],
            [4, 4, 3, 2, 1, 0, 0, 0, 0, 0],
            [4, 4, 3, 3, 2, 0, 0, 0, 0, 0],
            [4, 4, 4, 3, 2, 1, 0, 0, 0, 0],
            [4, 4 ,4, 3, 3, 2, 0, 0, 0, 0],
            [4, 4, 4, 4, 3, 2, 1, 0, 0, 0],
            [4, 4, 4, 4, 3, 3, 2, 0, 0, 0],
            [4, 4, 4, 4, 4, 3, 2, 1, 0, 0],
            [4, 4, 4, 4, 4, 3, 3, 2, 0, 0],
            [4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
            [4, 4, 4, 4, 4, 4, 3, 3, 2, 0],
            [4, 4, 4, 4, 4, 4, 4, 3, 2, 1],
            [4, 4, 4, 4, 4, 4, 4, 3, 3, 2],
            [4, 4, 4, 4, 4, 4, 4, 4, 3, 3],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
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

        self.spellsPrepared = []
        self.wizardSchool = ""

    def randomize(self, character):
        # Pick a random school specialization
        wizardSchools = ["abjuration", "conjuration", "divination", "enchantment", "illusion", "necromancy", "transmutation"]
        self.wizardSchool = wizardSchools[random.randint(0, len(wizardSchools) - 1)]

        # Pick some random spells the wizard might know.
        allWizardSpells = Spells.SpellList()
        allWizardSpells.loadFromFile("CharGen/Rulesets/Pathfinder/Data/Spells/Wizard.raw")

        # Pick our spells randomly
        intMod = character.getStatMod("int")
        spellsPerDay = self.getSpellsPerDay(character)
        spellLvl = 0
        for spellCount in spellsPerDay:
            # Pick spells.
            for i in range(1, spellCount):
                self.spellsPrepared += [allWizardSpells.getRandomSpell(spellLvl)]

            # Pick one more from the specialized school for each lvl.
            if spellCount > 0:
                self.spellsPrepared += [allWizardSpells.getRandomSpell(spellLvl, [self.wizardSchool])]
            spellLvl += 1



    def getSpellsPerDay(self, character):
        spellsPerDay = self.spellsKnown[self.level-1]

        # A character with a positive int mod might get extra spells slots.
        intMod = character.getStatMod("int")
        if intMod > 0:
            extraSpellsPerDay = self.extraSpellsPerDay[intMod]
            for i in range(0, len(extraSpellsPerDay) - 1):
                if spellsPerDay[i] == 0:
                    extraSpellsPerDay[i] = 0

            spellsPerDay = [x + y for x, y in list(zip(spellsPerDay, extraSpellsPerDay))]

        # A wizard needs at least 10 + spell level int to cast a spell.
        int = character.getStat("int")
        for i in range(0, len(spellsPerDay) - 1):
            if int < (10 + i):
                spellsPerDay[i] = 0

        return spellsPerDay

    def hd(self, character, total):
        return total + [(self.level, 6)]

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Wizard (" + self.wizardSchool + ")"]

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

    def weaponProficiency(self, character, total):
        total += ["Club", "Dagger", "Heavy Crossbow", "Light Crossbow", "Quarterstaff"]
        return total

    def spells(self, character, total):
        # Return with our spell list.
        wizardSpells = SpellList(self.level, "int")
        for spell in self.spellsPrepared:
            wizardSpells.addSpell(spell.name, spell.lvl)

        total["Wizard Spells"] = wizardSpells
        return total
