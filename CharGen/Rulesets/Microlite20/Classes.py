import math

class Commoner:
    def __init__(self, lvl):
        self.lvl = lvl

    def name(self, character, total):
        return total + ["Lvl " + str(self.lvl) + " Commoner"]

    def level(self, character, total):
        return total + self.lvl

class Fighter:
    def __init__(self, lvl):
        self.lvl = lvl

    def name(self, character, total):
        return total + ["Lvl " + str(self.lvl) + " Fighter"]

    def level(self, character, total):
        return self.lvl

    def physical(self, character, total):
        return total + 3

    def attackBonus(self, character, total):
        return total + 1  + math.floor(self.lvl / 5)

    def armorProficiency(self, character, total):
        return total + ["Light", "Medium", "Heavy", "Shield"]

class Rogue:
    def __init__(self, lvl):
        self.lvl = lvl

    def name(self, character, total):
        return total + ["Lvl " + str(self.lvl) + " Rogue"]

    def level(self, character, total):
        return self.lvl

    def subterfuge(self, character, total):
        return total + 3

    def abilities(self, character, total):
        return total + [("Sneak attack", "On sneak attack, add " + str(character.getSkill("subterfuge")) + " to damage")]

    def armorProficiency(self, character, total):
        return total + ["Light"]

class Magi:
    def __init__(self, lvl):
        self.lvl = lvl

    def name(self, character, total):
        return total + ["Lvl " + str(self.lvl) + " Magi"]

    def level(self, character, total):
        return self.lvl

    def knowledge(self, character, total):
        return total + 3

class Cleric:
    def __init__(self, lvl):
        self.lvl = lvl

    def name(self, character, total):
        return total + ["Lvl " + str(self.lvl) + " Cleric"]

    def level(self, character, total):
        return self.lvl

    def communication(self, character, total):
        return total + 3

    def abilities(self, character, total):
        return total + [("Turn Undead", "On a succesful magic attack turn undead. DC is the Hit Points of the Undead. If the DC is exceeded by 10 it is destroyed. Can be used " + str(2 + self.lvl + character.getStatBonus("mind")) + " times a day.")]

    def armorProficiency(self, character, total):
        return total + ["Light", "Medium"]
