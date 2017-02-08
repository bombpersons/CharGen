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
        self.spellsPerDay = [
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

    def getSpellsPerDay(self, character):
        spellsPerDay = self.spellsPerDay[self.level]

        intMod = character.getStatMod("int")
        if intMod > 0:

            #TODO prevent wizards of high int mod from casting spells beyond their level.

            extraSpellsPerDay = self.extraSpellsPerDay[intMod]
            combined = [x + y for x, y in list(zip(spellsPerDay, extraSpellsPerDay))]
            return combined

        return spellsPerDay

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

    def weaponProficiency(self, character, total):
        total["Club"] = True
        total["Dagger"] = True
        total["Heavy Crossbow"] = True
        total["Light Crossbow"] = True
        total["Quarterstaff"] = True

class WizardRandom(Wizard):
    def __init__(self, level):
        Wizard.__init__(self, level)

        # Store our int modifier
        self.storedIntMod = -100

        # Pick a random school specialization
        wizardSchools = ["abjuration", "conjuration", "divination", "enchantment", "illusion", "necromancy", "transmutation"]
        self.wizardSchool = wizardSchools[random.randint(0, len(wizardSchools) - 1)]

        # Pick some random spells the wizard might know.
        self.allWizardSpells = Spells.SpellList()
        self.allWizardSpells.loadFromFile("CharGen/Rulesets/Pathfinder/Data/Spells/Wizard.raw")

    def name(self, character, total):
        return Wizard.name(self, character, total) + ["(" + self.wizardSchool + ")"]

    def spells(self, character, total):
        # If our int modifier changed, we need to add / remove spells.
        intMod = character.getStatMod("int")
        if intMod != self.storedIntMod:
            self.spellsKnown = []
            spellsPerDay = self.getSpellsPerDay(character)
            spellLvl = 0
            for spellCount in spellsPerDay:
                for i in range(0, spellCount):
                    self.spellsKnown += [self.allWizardSpells.getRandomSpell(spellLvl)]

                # Pick one more from the specialized school for each lvl.
                if spellCount > 0:
                    self.spellsKnown += [self.allWizardSpells.getRandomSpell(spellLvl, [self.wizardSchool])]
                spellLvl += 1

            self.storedIntMod = intMod

        # Return with our spell list.
        wizardSpells = SpellList(self.level, "int")
        for spell in self.spellsKnown:
            wizardSpells.addSpell(spell.name, spell.lvl)

        total["Wizard Spells"] = wizardSpells
        return total
