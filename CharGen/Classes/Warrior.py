from CharGen.Character import *

class Warrior:
    def __init__(self, lvl):
        self.level = lvl

        self.goodSaveTable = {
            1 : 2,
            2 : 3,
            3 : 3,
            4 : 4,
            5 : 4,
            6 : 5,
            7 : 5,
            8 : 6,
            9 : 6,
            10 : 7,
            11 : 7,
            12 : 8,
            13 : 8,
            14 : 9,
            15 : 9,
            16 : 10,
            17 : 10,
            18 : 11,
            19 : 11,
            20 : 12
        }

        self.badSaveTable = {
            1 : 0,
            2 : 0,
            3 : 1,
            4 : 1,
            5 : 1,
            6 : 2,
            7 : 2,
            8 : 2,
            9 : 3,
            10 : 3,
            11 : 3,
            12 : 4,
            13 : 4,
            14 : 4,
            15 : 5,
            16 : 5,
            17 : 5,
            18 : 6,
            19 : 6,
            20 : 6
        }

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Warrior"]

    def hd(self, character, total):
        return total + [(self.level, 10)]

    def lvl(self, character, total):
        return total + self.level

    def BAB(self, character, total):
        return total + self.level

    def fortSave(self, character, total):
        return total + self.goodSaveTable[self.level]
    def refSave(self, character, total):
        return total + self.badSaveTable[self.level]
    def willSave(self, character, total):
        return total + self.badSaveTable[self.level]
