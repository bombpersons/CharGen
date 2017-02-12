import CharGen.Character as Character
import math

class Microlite20Character(Character.Character):
    def __init__(self):
        Character.Character.__init__(self)
        self.defaults = {
            # Name of character.
            "name" : [],

            # Base stats.
            "str" : 0,
            "dex" : 0,
            "mind" : 0,

            # Level
            "level" : 0,

            # Extra hp
            "extraHP" : 0,

            # Skills
            "physical" : 0,
            "subterfuge" : 0,
            "knowledge" : 0,
            "communication" : 0,
            "survival" : 0,
            "skillBonus" : 0,

            # Attack and Damage bonus
            "attackBonus" : 0,
            "damageBonus" : 0,

            # Armor proficiencies
            "armorProficiency" : [],

            # AC bonus
            "acBonus" : 0,

            # Abilities
            "abilities" : [],

            # attacks
            "attacks" : [],

            # gear
            "gear" : []
        }

    # Get name
    def getName(self):
        return " ".join(self.func("name"))

    # Get stats
    def getStat(self, stat):
        return self.func(stat)

    def getStatBonus(self, stat):
        return math.floor((self.getStat(stat) - 10) / 2)

    # Hit points and Hit dice
    def getHitDice(self):
        return (self.getLevel(), 6)

    def getHitPointBonus(self):
        return self.func("extraHP")

    def getHitPointAverage(self):
        return self.getLevel() * 3 + self.getHitPointBonus()

    # Level
    def getLevel(self):
        return self.func("level")

    # Spells
    def getSpellDC(self):
        return 10 + self.getLevel() + self.getStatBonus("mind")

    # Skill
    def getSkill(self, skill):
        return self.func(skill) + self.getLevel() + self.func("skillBonus")

    # Attack bonuses
    def getMeleeAttackBonus(self):
        return self.getStatBonus("str") + self.getLevel() + self.func("attackBonus")
    def getRangedAttackBonus(self):
        return self.getStatBonus("dex") + self.getLevel() + self.func("attackBonus")
    def getMagicAttackBonus(self):
        return self.getStatBonus("mind") + self.getLevel() + self.func("attackBonus")

    # Get any abilities
    def getAbilities(self):
        return self.func("abilities")

    # Get AC
    def getAC(self):
        return 10 + self.getStatBonus("dex") + self.func("acBonus")

    def getFlatAC(self):
        ac = 10 + self.func("acBonus")
        dexMod = self.getStatBonus("dex")
        if dexMod < 0:
            ac += dexMod
        return ac

    # Armor
    def getArmorProficiency(self):
        return self.func("armorProficiency")

    # Attacks
    def getAttacks(self):
        return self.func("attacks")

    # Gear
    def getGear(self):
        return self.func("gear")
