import random
from CharGen.Rulesets.Pathfinder.Rules import *

class Weapon:
    def __init__(self, name, dmg, critRange, critMult, range, dmgType, special, traits):
        self.name = name
        self.dmg = dmg
        self.critMult = critMult
        self.critRange = critRange
        self.range = range
        self.dmgType = dmgType
        self.special = special
        self.traits = traits

    def getAttack(self, character):
        attack = Attack(character)
        attack.name = self.name
        attack.dmgDice = self.dmg
        attack.critMult = self.critMult
        attack.critRange = self.critRange

        if "Ranged" in self.traits:
            attack.dmgStat = ""
            attack.toHitStat = "dex"
        else:
            attack.dmgStat = "str"
            attack.toHitStat = "str"

        return attack

class WeaponList:
    def __init__(self):
        self.set = {}

    def addWeapon(self, weapon):
        self.set[weapon.name] = weapon

    def getWeapon(self, name):
        return self.set[name]

    def getRandomWeapon(self, traits):
        # Gather weapons that match the required traits.
        potential = []
        for weapon in self.set.values():
            found = True
            for trait in traits:
                if trait not in weapon.traits:
                    found = False

            if found:
                potential += [weapon]

        if len(potential) == 0:
            return None

        # Pick one entirely at random.
        r = random.randint(0, len(potential) - 1)
        return potential[r]

class WesternWeaponList(WeaponList):
    def __init__(self):
        WeaponList.__init__(self)

        self.addWeapon(Weapon("Gauntlet", (1, 3), 20, 2, 0, ["B"], [], ["Simple", "Unarmed Attack"]))
        self.addWeapon(Weapon("Unarmed Strike", (1, 3), 20, 2, 0, ["B"], ["nonlethal"], ["Simple", "Unarmed Atack"]))

        self.addWeapon(Weapon("Battle aspergillum", (1, 6), 2, 20, 0, ["B"], [], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Brass Knife", (1, 4), 19, 2, 10, ["P", "S"], ["fragile"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Brass Knuckles", (1, 3), 20, 2, 0, ["B"], ["monk"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Cestus", (1, 4), 19, 2, 0, ["B", "P"], ["monk"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Dagger", (1, 4), 19, 2, 10, ["P", "S"], [], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Dagger, punching", (1, 4), 20, 3, 0, ["P"], [], ["Simple", "Light", "One-Handed"]))
        #TODO ADD MORE

        self.addWeapon(Weapon("Club", (1, 6), 20, 2, 10, ["B"], [], ["Simple", "One-Handed"]))

        self.addWeapon(Weapon("Spear", (1, 8), 20, 3, 20, ["P"], ["brace"], ["Simple", "Two-Handed"]))
