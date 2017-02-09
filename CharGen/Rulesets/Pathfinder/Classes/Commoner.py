from CharGen.Rulesets.Pathfinder import *
import CharGen.Rulesets.Pathfinder.Weapons as Weapons

class Commoner:
    def __init__(self, lvl):
        self.level = lvl

        self.badSaveTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.babTable = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

        self.weaponProf = ""

    def randomize(self, character):
        # Commoners have proficiency with a single random simple weapon.
        weaponList = Weapons.WeaponList()
        weapon = weaponList.getRandomWeapon(["Simple"])
        self.weaponProf = weapon.name

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Commoner"]

    def hd(self, character, total):
        return total + [(self.level, 6)]

    def lvl(self, character, total):
        return total + self.level

    def BAB(self, character, total):
        return total + self.babTable[self.level]

    def fortSaveBonus(self, character, total):
        return total + self.badSaveTable[self.level]
    def refSaveBonus(self, character, total):
        return total + self.badSaveTable[self.level]
    def willSaveBonus(self, character, total):
        return total + self.badSaveTable[self.level]

    def skills(self, character, total):
        total["Climb"].classSkill = True
        #total["Craft ()"].classSkill = True
        total["Handle Animal"].classSkill = True
        total["Perception"].classSkill = True
        #total["Profession ()"].classSkill = True
        total["Ride"].classSkill = True
        total["Swim"].classSkill = True

        return total

    def skillRanks(self, character, total):
        return total + 2 * self.level

    def weaponProficiency(self, character, total):
        return total + [self.weaponProf]
