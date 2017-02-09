import random
from CharGen.Rulesets.Pathfinder.Rules import *

class ArmorTemplate:
    def __init__(self, armor):
        self.armor = armor

    def armorACBonus(self, character, total):
        return total + self.armor.ACBonus

    def armorCheckPenalty(self, character, total):
        return total + self.armor.ACP

    def maxDexBonus(self, character, total):
        return self.armor.maxDexBonus if total > self.armor.maxDexBonus else total

    def spellFailureChance(self, character, total):
        return total + self.armor.spellFailure

    def gear(self, character, total):
        return total + [self.armor.name]

class Armor:
    def __init__(self, name, ACBonus, maxDexBonus, ACP, spellFailure, mediumSpeed, smallSpeed, traits):
        self.name = name
        self.ACBonus = ACBonus
        self.maxDexBonus = maxDexBonus
        self.ACP = ACP
        self.spellFailure = spellFailure

        self.mediumSpeed = mediumSpeed
        self.smallSpeed = smallSpeed

        self.traits = traits

class ArmorList:
    def __init__(self):
        self.set = {}

        # Light armor.
        self.addArmor(Armor("Padded", 1, 6, 0, 0, 30, 20, ["Light"]))
        self.addArmor(Armor("Quilted Cloth", 1, 8, 0, 5, 30, 20, ["Light"]))
        self.addArmor(Armor("Leather", 2, 8, 0, 10, 30, 20, ["Light"]))
        self.addArmor(Armor("Rosewood armor", 2, 6, 0, 10, 30, 20, ["Light"]))
        self.addArmor(Armor("Hide shirt", 3, 4, 1, 15, 30, 20, ["Light"]))
        self.addArmor(Armor("Leaf armor", 3, 5, 0, 15, 30, 20, ["Light"]))
        self.addArmor(Armor("Parade armor", 3, 5, 1, 15, 30, 20, ["Light"]))
        self.addArmor(Armor("Studded leather", 3, 5, 1, 15, 30, 20, ["Light"]))
        self.addArmor(Armor("Wooden", 3, 3, 1, 15, 30, 20, ["Light"]))
        self.addArmor(Armor("Chain shirt", 4, 4, 2, 20, 30, 20, ["Light"]))

        # Medium armor
        self.addArmor(Armor("Armored coat", 4, 3, 2, 20, 20, 15, ["Medium"]))
        self.addArmor(Armor("Hide", 4, 4, 3, 20, 20, 15, ["Medium"]))
        self.addArmor(Armor("Scale mail", 5, 3, 4, 25, 20, 15, ["Medium"]))
        self.addArmor(Armor("Chainmail", 6, 2, 5, 30, 20, 15, ["Medium"]))
        self.addArmor(Armor("Breastplate", 6, 3, 4, 25, 20, 15, ["Medium"]))
        self.addArmor(Armor("Breastplate (agile)", 6, 3, 4, 25, 20, 15, ["Medium"]))

        # Heavy armor
        self.addArmor(Armor("Splint mail", 7, 0, 7, 40, 20, 15, ["Heavy"]))
        self.addArmor(Armor("Banded mail", 7, 1, 6, 35, 20, 15, ["Heavy"]))
        self.addArmor(Armor("Field plate", 7, 1, 5, 35, 20, 15, ["Heavy"]))
        self.addArmor(Armor("Half-plate", 8, 0, 7, 40, 20, 15, ["Heavy"]))
        self.addArmor(Armor("Half-plate (agile)", 8, 0, 7, 40, 20, 15, ["Heavy"]))
        self.addArmor(Armor("Full plate", 9, 1, 6, 35, 20 ,15, ["Heavy"]))
        self.addArmor(Armor("Hellknight plate", 9, 1, 5, 35, 20, 15, ["Heavy"]))
        self.addArmor(Armor("Soneplate", 9, 1, 6, 35, 15, 10, ["Heavy"]))

        # Shields
        self.addArmor(Armor("Buckler", 1, 99, 1, 5, 0, 0, ["Shield"]))
        self.addArmor(Armor("Klar", 1, 99, 1, 5, 0, 0, ["Shield"]))
        self.addArmor(Armor("Madu", 1, 99, 2, 5, 0, 0, ["Shield"]))
        self.addArmor(Armor("Light Wooden Shield", 1, 99, 1, 5, 0, 0, ["Shield"]))
        self.addArmor(Armor("Heavy Wooden Shield", 2, 99, 2, 15, 0, 0, ["Shield"]))
        self.addArmor(Armor("Heavy Steel Shield", 2, 99, 2, 15, 0, 0, ["Shield"]))
        self.addArmor(Armor("Tower Shield", 4, 2, 10, 50, 0, 0, ["Shield"]))

    def addArmor(self, armor):
        self.set[armor.name] = armor

    def getRandomArmor(self, traits):
        # Gather weapons that match the required traits.
        potential = self.getArmors(traits)
        if len(potential) == 0:
            return None

        # Pick one entirely at random.
        r = random.randint(0, len(potential) - 1)
        return potential[r]

    def getArmors(self, traits):
        armors = []
        for armor in self.set.values():
            found = True
            for trait in traits:
                if trait not in armor.traits:
                    found = False

            if found:
                armors += [armor]
        return armors
