import random
from CharGen.Rulesets.Pathfinder.Rules import *

class WeaponTemplate:
    def __init__(self, weapon):
        self.weapon = weapon

    def melee(self, character, total):
        if "Ranged" in self.weapon.traits:
            return total

        total += [self.weapon.getAttack(character)]
        return total

    def ranged(self, character, total):
        if "Ranged" not in self.weapon.traits:
            return total

        total += [self.weapon.getAttack(character)]
        return total

    def gear(self, character, total):
        return total + [self.weapon.name]

class Weapon:
    def __init__(self, name, dmg, critRange, critMult, range, dmgType, traits):
        self.name = name
        self.dmg = dmg
        self.critMult = critMult
        self.critRange = critRange
        self.range = range
        self.dmgType = dmgType
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

        # Simple weapons.
        self.addWeapon(Weapon("Gauntlet", (1, 3), 20, 2, 0, ["B"], ["Simple", "Unarmed Attack"]))
        self.addWeapon(Weapon("Unarmed Strike", (1, 3), 20, 2, 0, ["B"], ["nonlethal", "Simple", "Unarmed Atack"]))

        self.addWeapon(Weapon("Battle aspergillum", (1, 6), 2, 20, 0, ["B"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Brass Knife", (1, 4), 19, 2, 10, ["P", "S"], ["fragile", "Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Brass Knuckles", (1, 3), 20, 2, 0, ["B"], ["monk", "Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Cestus", (1, 4), 19, 2, 0, ["B", "P"], ["monk", "Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Dagger", (1, 4), 19, 2, 10, ["P", "S"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Dagger, punching", (1, 4), 20, 3, 0, ["P"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Spiked Gauntlet", (1, 4), 20, 2, 0, ["P"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Hook hand", (1, 4), 20, 2, 0, ["S"], ["disarm", "Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Kunai", (1, 4), 20, 2, 10, ["B", "P"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Light Mace", (1, 6), 20, 2, 0, ["B"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Sickle", (1, 6), 20, 2, 0, ["S"], ["trip", "Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Spring blade", (1, 4), 20, 2, 10, ["P", "S"], ["Simple", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Wooden stake", (1, 4), 20, 2, 10, ["P"], ["Simple", "Light", "One-Handed"]))

        self.addWeapon(Weapon("Club", (1, 6), 20, 2, 10, ["B"], ["Simple", "One-Handed"]))
        self.addWeapon(Weapon("Mere Club", (1, 4), 20, 2, 0, ["B", "P"], ["fragile", "Simple", "One-Handed"]))
        self.addWeapon(Weapon("Heavy Mace", (1, 8), 20, 2, 0, ["B"], ["Simple", "One-Handed"]))
        self.addWeapon(Weapon("Morningstar", (1, 8), 20, 2, 0, ["B", "P"], ["Simple", "One-Handed"]))
        self.addWeapon(Weapon("Shortspear", (1, 6), 20, 2, 20, ["P"], ["Simple", "One-Handed"]))

        self.addWeapon(Weapon("Boarding Pike", (1, 8), 20, 3, 0, ["P"], ["brace", "reach", "Simple", "Two-Handed"]))
        self.addWeapon(Weapon("Kumade", (1, 6), 20, 3, 0, ["P"], ["grapple", "Simple", "Two-Handed"]))
        self.addWeapon(Weapon("Collapsible Kumade", (1, 6), 20, 3, 0, ["P"], ["grapple", "Simple", "Two-Handed"]))
        self.addWeapon(Weapon("Longspear", (1, 8), 20, 3, 0, ["P"], ["brace", "reach", "Simple", "Two-Handed"]))
        self.addWeapon(Weapon("Quarterstaff", (1, 6), 20, 2, 0, ["B"], ["double", "monk", "Simple", "Two-Handed"]))
        self.addWeapon(Weapon("Spear", (1, 8), 20, 3, 20, ["P"], ["brace", "Simple", "Two-Handed"]))
        self.addWeapon(Weapon("Boar Spear", (1, 8), 20, 2, 0, ["P"], ["brace", "Simple", "Two-Handed"]))
        self.addWeapon(Weapon("Weighted Spear", (1, 8), 20, 3, 0, ["P"], ["brace", "double", "Simple", "Two-Handed"]))

        self.addWeapon(Weapon("Blowgun", (1, 2), 20, 2, 20, ["P"], ["Simple", "Ranged"]))
        self.addWeapon(Weapon("Heavy Crossbow", (1, 10), 19, 2, 120, ["P"], ["Simple", "Ranged"]))
        self.addWeapon(Weapon("Light Crossbow", (1, 8), 19, 2, 80, ["P"], ["Simple", "Ranged"]))
        self.addWeapon(Weapon("Dart", (1, 4), 20, 2, 20, ["P"], ["Simple", "Ranged"]))
        self.addWeapon(Weapon("Javelin", (1, 6), 20, 2, 30, ["P"], ["Simple", "Ranged"]))
        self.addWeapon(Weapon("Sling", (1, 4), 20, 2, 50, ["B"], ["Simple", "Ranged"]))
        self.addWeapon(Weapon("Stingchuck", (1, 4), 20, 2, 10, ["B"], ["Simple", "Ranged"]))
        self.addWeapon(Weapon("Stonebow", (1, 6), 20, 2, 50, ["B"], ["Simple", "Ranged"]))

        # Martial weapons.
        self.addWeapon(Weapon("Boarding Axe", (1, 6), 20, 3, 0, ["P", "S"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Throwing Axe", (1, 6), 20, 2, 10, ["S"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Cat-o'-nine-tails", (1, 4), 20, 2, 0, ["S"], ["disarm", "nonlethal", "Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Dogslicer", (1, 6), 19, 2, 0, ["S"], ["fragile", "Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Light Hammer", (1, 4), 20, 2, 20, ["B"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Gladius", (1, 6), 19, 2, 0, ["P", "S"], ["performance", "Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Handaxe", (1, 6), 20, 3, 0, ["S"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Switchblade Knife", (1, 4), 19, 2, 10, ["P"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Kukri", (1, 4), 18, 2, 0, ["S"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Machete", (1, 6), 19, 2, 0, ["S"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Light Pick", (1, 4), 20, 4, 0, ["P"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Sap", (1, 6), 20, 2, 0, ["B"], ["nonlethal", "Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Sea-Knife", (1, 4), 19, 2, 0, ["S"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Starknife", (1, 4), 20, 3, 20, ["P"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("Short Sword", (1, 6), 19, 2, 0, ["P"], ["Martial", "Light", "One-Handed"]))
        self.addWeapon(Weapon("War Razor", (1, 4), 19, 2, 0, ["S"], ["Martial", "Light", "One-Handed"]))

        self.addWeapon(Weapon("Ankus", (1, 8), 20, 2, 0, ["P"], ["disam", "trip", "Martial", "One-Handed"]))
        self.addWeapon(Weapon("Battleaxe", (1, 8), 20, 3, 0, ["S"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Combat scabbard", (1, 6), 20, 2, 0, ["B"], ["improvised", "Martial", "One-Handed"]))
        self.addWeapon(Weapon("Cutlass", (1, 6), 18, 2, 0, ["S"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Flail", (1, 8), 20, 2, 0, ["B"], ["disarm", "trip", "Martial", "One-handed"]))
        self.addWeapon(Weapon("Gandasa", (2, 4), 20, 3, 0, ["S"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Klar", (1, 6), 20, 2, 0, ["S"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Longsword", (1, 8), 19, 2, 0, ["S"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Manople", (1, 8), 20, 2, 0, ["P", "S"], ["blocking", "disarm", "Martial", "One-Handed"]))
        self.addWeapon(Weapon("Heavy Pick", (1, 6), 20, 4, 0, ["P"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Rapier", (1, 6), 18, 2, 0, ["P"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Scimitar", (1, 6), 18, 2, 0, ["S"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Scizore", (1, 10), 20, 2, 0, ["P"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Sword Cane", (1, 6), 20, 2, 0, ["P"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Trebutje", (1, 8), 19, 2, 0, ["S"], ["fragile", "Martial", "One-Handed"]))
        self.addWeapon(Weapon("Steel Trebutje", (1, 8), 19, 2, 0, ["S"], ["Martial", "One-Handed"]))
        self.addWeapon(Weapon("Trident", (1, 8), 20, 2, 0, ["P"], ["brace", "Martial", "One-Handed"]))
        self.addWeapon(Weapon("Warhammer", (1, 8), 20, 3, 0, ["B"], ["Martial", "One-Handed"]))

        self.addWeapon(Weapon("Bardiche", (1, 10), 19, 2, 0, ["S"], ["brace", "reach", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Bec de corbin", (1, 10), 20, 3, 0, ["B", "P"], ["brace", "reach", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Bill", (1, 8), 20, 3, 0, ["S"], ["brace", "disarm", "reach", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Earth Breaker", (2, 6), 20, 3, 0, ["B"], ["Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Falchion", (2, 4), 18, 2, 0, ["S"], ["Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Heavy Flail", (1, 10), 19, 2, 0, ["B"], ["disarm", "trip", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Glaive", (1, 10), 20, 3, 0, ["S"], ["reach", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Glaive-guisarme", (1, 10), 20, 3, 0, ["S"], ["brace", "reach", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Greataxe", (1, 12), 20, 3, 0, ["S"], ["Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Greatclub", (1, 10), 20, 2, 0, ["B"], ["Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Greatsword", (2, 6), 19, 2, 0, ["S"], ["Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Guisarme", (2, 4), 20, 3, 0, ["S"], ["reach", "trip", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Halberd", (1, 10), 20, 3, 0, ["P", "S"], ["brace", "trip", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Lucerne Hammer", (1, 12), 20, 2, 0, ["B", "P"], ["brace", "reach", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Horsechopper", (1, 10), 20, 3, 0, ["P", "S"], ["reach", "trip", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Lance", (1, 8), 20, 3, 0, ["P"], ["reach", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Ogre hook", (1, 10), 20, 3, 0, ["P"], ["trip", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Pickaxe", (1, 8), 20, 4, 0, ["P"], ["Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Planson", (1, 10), 20, 2, 0, ["B", "P"], ["brace", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Ranseur", (2, 4), 20, 3, 0, ["P"], ["disarm", "reach", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Scythe", (2, 4), 20, 4, 0, ["P", "S"], ["trip", "Martial", "Two-Handed"]))
        self.addWeapon(Weapon("Syringe Spear", (1, 8), 20, 3, 20, ["P"], ["brace", "Martial", "Two-Handed"]))

        self.addWeapon(Weapon("Ammentum", (1, 6), 20, 2, 50, ["P"], ["performance", "Martial", "Ranged"]))
        self.addWeapon(Weapon("Chakram", (1, 8), 20, 2, 30, ["S"], ["Martial", "Ranged"]))
        self.addWeapon(Weapon("Hunga munga", (1, 6), 20, 2, 15, ["P"], ["Martial", "Ranged"]))
        self.addWeapon(Weapon("Hurlbat", (1, 6), 20, 3, 10, ["P", "S"], ["Martial", "Ranged"]))
        self.addWeapon(Weapon("Longbow", (1, 8), 20, 3, 100, ["P"], ["Martial", "Ranged"]))
        self.addWeapon(Weapon("Pilum", (1, 8), 20, 2, 20, ["P"], ["Martial", "Ranged"]))
        self.addWeapon(Weapon("Shortbow", (1, 6), 20, 3, 60, ["P"], ["Martial", "Ranged"]))

        # TODO exotic weapons.

    def addWeapon(self, weapon):
        self.set[weapon.name] = weapon

    def getWeapon(self, name):
        return self.set[name]

    def getRandomWeapon(self, traits):
        # Gather weapons that match the required traits.
        potential = self.getWeapons(traits)
        if len(potential) == 0:
            return None

        # Pick one entirely at random.
        r = random.randint(0, len(potential) - 1)
        return potential[r]

    def getWeapons(self, traits):
        weapons = []
        for weapon in self.set.values():
            found = True
            for trait in traits:
                if trait not in weapon.traits:
                    found = False

            if found:
                weapons += [weapon]
        return weapons
