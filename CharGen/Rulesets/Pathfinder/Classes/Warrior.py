from CharGen.Rulesets.Pathfinder import *

class Warrior:
    def __init__(self, lvl):
        self.level = lvl

        self.badSaveTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.goodSaveTable = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Warrior"]

    def hd(self, character, total):
        return total + [(self.level, 10)]

    def lvl(self, character, total):
        return total + self.level

    def BAB(self, character, total):
        return total + self.level

    def fortSaveBonus(self, character, total):
        return total + self.goodSaveTable[self.level]
    def refSaveBonus(self, character, total):
        return total + self.badSaveTable[self.level]
    def willSaveBonus(self, character, total):
        return total + self.badSaveTable[self.level]

    def skills(self, character, total):
        total["Climb"].classSkill = True
        #total["Craft ()"].classSkill = True
        total["Handle Animal"].classSkill = True
        total["Intimidate"].classSkill = True
        #total["Profession ()"].classSkill = True
        total["Ride"].classSkill = True
        total["Swim"].classSkill = True

        return total
