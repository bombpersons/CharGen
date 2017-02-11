from CharGen.Rulesets.Pathfinder import *

import random

class Aristocrat:
    def __init__(self, lvl):
        self.level = lvl

        self.babTable = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.badSaveTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.goodSaveTable = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Aristocrat"]

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
        total["Appraise"].classSkill = True
        total["Bluff"].classSkill = True
        total["Diplomacy"].classSkill = True
        total["Disguise"].classSkill = True
        total["Handle Animal"].classSkill = True
        total["Intimidate"].classSkill = True
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
        total["Linguistics"].classSkill = True
        total["Perception"].classSkill = True
        #total["Perform ()"].classSkill = True
        #total["Profession ()"].classSkill = True
        total["Ride"].classSkill = True
        total["Sense Motive"].classSkill = True
        total["Swim"].classSkill = True
        total["Survival"].classSkill = True

        return total

    def skillRanks(self, character, total):
        return total + 4 * self.level

    def weaponTraitProficiency(self, character, total):
        return total + ["Simple" + "Martial"]

    def armorTraitProficiency(self, character, total):
        return total + ["Light", "Medium", "Heavy", "Shield"]
