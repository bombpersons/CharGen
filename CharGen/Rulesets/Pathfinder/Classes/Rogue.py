from CharGen.Rulesets.Pathfinder import *

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

    def name(self, character, total):
        return total + ["Lvl " + str(self.level) + " Rogue"]

    def hd(self, character, total):
        return total + [(self.level, 10)]

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
        total["Knowledeg (Local)"].classSkill = True
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
        return total + 2 * self.level

    def weaponTraitProficiency(self, character, total):
        return total + ["Simple"]

    def weaponProficiency(self, character, total):
        return total + ["Hand Crossbow", "Rapier", "Sap", "Shortbow", "Shortsword"]

    def armorTraitProficiency(self, character, total):
        return total + ["Light"]

    def abilities(self, character, total):
        newAbilities = []
        if self.level >= 2:
            evasion = Ability()
            evasion.name = "Evasion (Ex)"
            evasion.desc = "At 2nd level and higher, a rogue can avoid even magical and unusual attacks with great agility. If she makes a successful Reflex saving throw against an attack that normally deals half damage on a successful save, she instead takes no damage. Evasion can be used only if the rogue is wearing light armor or no armor. A helpless rogue does not gain the benefit of evasion."
            newAbilities += [evasion]

        if self.level >= 3:
            trapSense = Ability()
            trapSense.name = "Trap Sense (Ex)"
            trapSense.desc = "At 3rd level, a rogue gains an intuitive sense that alerts her to danger from traps, giving her a +1 bonus on Reflex saves made to avoid traps and a +1 dodge bonus to AC against attacks made by traps. These bonuses rise to +2 when the rogue reaches 6th level, to +3 when she reaches 9th level, to +4 when she reaches 12th level, to +5 at 15th, and to +6 at 18th level. Trap sense bonuses gained from multiple classes stack."
            newAbilities += [trapSense]

        return total + newAbilities
