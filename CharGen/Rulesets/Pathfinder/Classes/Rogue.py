from CharGen.Rulesets.Pathfinder.Rules import *

class Rogue:
    def __init__(self, lvl):
        self.level = lvl

        self.babTable = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.badSaveTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.goodSaveTable = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.sneakDmgTable = [
            (1, 6), (1, 6),
            (2, 6), (2, 6),
            (3, 6), (3, 6),
            (4, 6), (4, 6),
            (5, 6), (5, 6),
            (6, 6), (6, 6),
            (7, 6), (7, 6),
            (8, 6), (8, 6),
            (9, 6), (9, 6),
            (10, 6), (10, 6)
        ]
        self.trapSenseTable = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6]

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Rogue"]

    def hd(self, character, total):
        return total + [(self.level, 8)]

    def lvl(self, character, total):
        return total + self.level

    def BAB(self, character, total):
        return total + self.babTable[self.level]

    def fortSaveBonus(self, character, total):
        return total + self.badSaveTable[self.level]
    def refSaveBonus(self, character, total):
        return total + self.goodSaveTable[self.level]
    def willSaveBonus(self, character, total):
        return total + self.badSaveTable[self.level]

    def skills(self, character, total):
        total["Acrobatics"].classSkill = True
        total["Appraise"].classSkill = True
        total["Bluff"].classSkill = True
        total["Climb"].classSkill = True
        #total["Craft ()"].classSkill = True
        total["Diplomacy"].classSkill = True
        total["Disable Device"].classSkill = True
        total["Disguise"].classSkill = True
        total["Escape Artist"].classSkill = True
        total["Intimidate"].classSkill = True
        total["Knowledge (Dungeoneering)"].classSkill = True
        total["Knowledge (Local)"].classSkill = True
        total["Linguistics"].classSkill = True
        total["Perception"].classSkill = True
        #total["Perform"].classSkill = True
        #total["Profession ()"].classSkill = True
        total["Sense Motive"].classSkill = True
        total["Sleight of Hand"].classSkill = True
        total["Stealth"].classSkill = True
        total["Swim"].classSkill = True
        total["Use Magic Device"].classSkill = True

        return total

    def skillRanks(self, character, total):
        return total + 8 * self.level

    def weaponTraitProficiency(self, character, total):
        return total + ["Simple"]

    def weaponProficiency(self, character, total):
        return total + ["Hand Crossbow", "Rapier", "Sap", "Shortbow", "Short Sword"]

    def armorTraitProficiency(self, character, total):
        return total + ["Light"]

    def abilities(self, character, total):
        newAbilities = []
        sneakAttackDice = self.sneakDmgTable[self.level]
        newAbilities += [Ability("Sneak Attack", "Add " + str(sneakAttackDice[0]) + "d" + str(sneakAttackDice[1]) + " damage to target when flanked or flat-footed.")]

        if self.level >= 2:
            ab = Ability("Evasion (Ex)", \
                         "Take no damage on succesful reflex saves rather than half.")
            newAbilities += [ab]

        if self.level >= 3:
            ab = Ability("Trap Sense (Ex)", \
                         "Get a +" + str(self.trapSenseTable[self.level]) + " on reflex saves and AC against traps.")
            newAbilities += [ab]

        if self.level >= 4:
            ab = Ability("Uncanny Dodge (Ex)", \
                        "Can't be caught flat-footed (can still be feinted).")
            newAbilities += [ab]

        if self.level >= 8:
            ab = Ability("Improved Uncanny Dodge (Ex)", \
                        "Can't be flanked unless the attacker is a rogue of level " + str(self.level+4) + " or higher.")
            newAbilities += [ab]

        if self.level >= 20:
            ab = Ability("Master Strike (Ex)", \
                         "Whenever the rogue deals a sneak attack, they may choose to put the target to sleep for 1d4 hours, paralyze them for 2d6 rounds, or kill them")
            newAbilities += [ab]

        return total + newAbilities
