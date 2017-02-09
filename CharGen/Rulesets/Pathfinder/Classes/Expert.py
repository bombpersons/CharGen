from CharGen.Rulesets.Pathfinder import *

import random

class Expert:
    def __init__(self, lvl):
        self.level = lvl

        self.babTable = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.badSaveTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.goodSaveTable = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]

        self.classSkills = []

    def randomize(self, character):
        # Experts get
        skills = character.getSkillList()[:]
        for i in range(1, 10):
            skill = skills[random.randint(0, len(skills) - 1)]
            self.classSkills += [skill]
            skills.remove(skill)

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Expert"]

    def hd(self, character, total):
        return total + [(self.level, 8)]

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
        for skill in self.classSkills:
            total[skill].classSkill = True
        return total

    def skillRanks(self, character, total):
        return total + 6 * self.level

    def weaponTraitProficiency(self, character, total):
        return total + ["Simple"]

    def armorTraitProficiency(self, character, total):
        return total + ["Light"]
