import CharGen.Dice as Dice
from CharGen.Character import *

import math
from enum import Enum

# useful function to convert an integer like 3 to +3
def numToBonusString(n, includeZero=True, before="", after=""):
    if n < 0:
        return before + "-" + after + str(abs(n))
    elif n > 0:
        return before + "+" + after + str(n)
    else:
        return str(n) if includeZero else ""

# Sizes for characters.
def speedFromSize(size):
    if size == "Small":
        return 20
    elif size == "Medium":
        return 30

def getSizeModifier(size):
    if size == "Small":
        return 1
    elif size == "Medium":
        return 0

def getStealthSkillModifierBasedOnSize(size):
    if size == "Small":
        return 4
    elif size == "Medium":
        return 0

# Vision for characters.
class Vision(Enum):
    NORMAL=1
    LOW_LIGHT=2
    DARK=3

def getModifier(score):
    normalised = score - 10
    return math.floor(normalised / 2)

# Sex of characeters.
class Sex(Enum):
    MALE=1,
    FEMALE=2,
    NOT_APPLICABLE=3

def getDiceString(dice, bonus=0, before="", after=""):
    return str(dice[0]) + "d" + str(dice[1]) + numToBonusString(bonus, includeZero=False, before=before, after=after)

def getDiceSetString(dice, bonus=0, before="", after=""):
    s = ""
    if len(dice) == 0:
        s = str(bonus)
    else:
        for i in range(0, len(dice)):
            item = dice[i]

            # Add a + if this is an extra set of hd
            if i != 0:
                if item[0] > 0:
                    s += "+"

            s += getDiceString(item)
        s += numToBonusString(bonus, includeZero=False, before=before, after=after)
    return s

# Class that defines an attack. Specifies a to hit bonus as well as damage and any other effects.
class Attack:
    def __init__(self, character):
        self.toHitStat = ""
        self.dmgStat = ""
        self.dmgDice = (0, 0)

        self.dmgExtraDice = (0, 0)
        self.dmgExtraType = ""

        self.enhancement = 0
        self.masterwork = False

        self.critRange = 20
        self.critMult = 2
        self.twoHanded = False
        self.primary = True
        self.natural = False
        self.proficient = True

        self.name = ""
        self.character = character

    def getDmgMod(self):
        dmgMod = 0

        if self.dmgStat != "":
            # Secondary attacks only use half the str bonus.
            if not self.primary and self.dmgStat == "str":
                dmgMod += math.floor(getModifier(self.character.func(self.dmgStat)) * 0.5)
            # Characters who use both hands and use strength get extra strength dmg.
            elif self.twoHanded and self.dmgStat == "str":
                dmgMod += math.floor(getModifier(self.character.func(self.dmgStat)) * 1.5)
            else:
                dmgMod += math.floor(getModifier(self.character.func(self.dmgStat)))

        dmgMod += self.enhancement

        return dmgMod;

    def getToHit(self):
        toHit = self.character.func("BAB") + getSizeModifier(self.character.func("size"))

        if self.toHitStat != "":
            toHit += getModifier(self.character.func(self.toHitStat))

        # Secondary attacks are made at a -5 penalty.
        if not self.primary:
            toHit -= 5

        # Attacks with weapons the character is not proficient with are taken at a -4 penalty.
        if not self.proficient:
            toHit -= 4

        # Masterwork doesn't stack with enhancement
        if self.masterwork and self.enhancement == 0:
            toHit += 1
        toHit += self.enhancement

        return toHit

    def __str__(self):
        s = self.name + " " + numToBonusString(self.getToHit()) + " "
        s += "(" + getDiceString(self.dmgDice, self.getDmgMod())

        if self.critMult != 2 or self.critRange != 20:
            s += "/"
            if self.critRange != 20:
                s += str(self.critRange) + "-20"
            if self.critMult != 2:
                s += "x" + str(self.critMult)

        if self.dmgExtraDice[0] > 0:
            s += " plus " + getDiceString(self.dmgExtraDice)
            if self.dmgExtraType != "":
                s += " " + self.dmgExtraType

        s += ")"
        return s

# skills
class Skill:
    def __init__(self, stat):
        self.stat = stat
        self.ranks = 0
        self.classSkill = False

# special abilities
class Ability:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

# spells
class SpellList:
    def __init__(self, casterLevel=1, castingStat="int"):
        self.spells = {}
        self.spellsPerDay = {}
        self.casterLevel = casterLevel
        self.castingStat = castingStat

    def setSpellsPerDay(self, lvl, num):
        self.spellsPerDay[lvl] = num

    def addSpell(self, name, lvl):
        if lvl not in self.spells:
            self.spells[lvl] = {}

        if name not in self.spells[lvl]:
            self.spells[lvl][name] = 1
        else:
            self.spells[lvl][name] += 1

    def getSpells(self, lvl):
        if lvl in self.spells:
            return self.spells[lvl]
        return {}

    def getSpellsPerDay(self, lvl):
        if lvl in self.spellsPerDay:
            return self.spellsPerDay[lvl]
        return 0

    def getCasterLevel(self):
        return self.casterLevel

    def getConcentrationBonus(self, character):
        return getModifier(character.func(self.castingStat)) + self.casterLevel

    def getDC(self, character, lvl):
        return 10 + getModifier(character.func(self.castingStat)) + lvl

    def isEmpty(self):
        return len(self.spells) == 0


class PathfinderCharacter(Character):
    def __init__(self):
        Character.__init__(self)
        self.defaults = {
            "str" : 0,
            "dex" : 0,
            "con" : 0,
            "int" : 0,
            "wis" : 0,
            "cha" : 0,

            "sex" : Sex.MALE,
            "type" : "Humanoid",
            "size" : "Medium",
            "speed" : 0,

            "name" : [],
            "vision" : [],

            # Initiative and stats used to calculate it.
            "initStats" : ["dex"],
            "initBonus" : 0,

            # Hit Dice and Stats used to caculate extra hitpoints.
            "hd" : [],
            "hpStats" : ["con"],

            "lvl" : 0,

            # AC bonuses
            "naturalACBonus" : 0,
            "dodgeACBonus" : 0,
            "deflectACBonus" : 0,
            "miscACBonus" : 0,
            "armorACBonus" : 0,
            "shieldACBonus" : 0,
            "ACStats" : ["dex"],

            # Saves
            "fortSaveStats" : ["con"],
            "fortSaveBonus" : 0,
            "refSaveStats" : ["dex"],
            "refSaveBonus" : 0,
            "willSaveStats" : ["wis"],
            "willSaveBonus" : 0,

            "BAB" : 0,

            "CMBBonus" : 0,
            "CMBStats" : ["str"],

            "CMDBonus" : 0,
            "CMDStats1" : ["str"],
            "CMDStats2" : ["dex"],

            "melee" : [],
            "ranged" : [],

            "abilities" : [],

            "skills" : {
                "Acrobatics" : Skill("dex"),
                "Appraise" : Skill("int"),
                "Bluff" : Skill("cha"),
                "Climb" : Skill("str"),
                "Diplomacy" : Skill("cha"),
                "Disable Device" : Skill("dex"),
                "Disguise" : Skill("cha"),
                "Escape Artist" : Skill("dex"),
                "Fly" : Skill("dex"),
                "Handle Animal" : Skill("cha"),
                "Heal" : Skill("wis"),
                "Intimidate" : Skill("cha"),
                "Knowledge (Arcana)" : Skill("int"),
                "Knowledge (Dungeoneering)" : Skill("int"),
                "Knowledge (Geography)" : Skill("int"),
                "Knowledge (History)" : Skill("int"),
                "Knowledge (Local)" : Skill("int"),
                "Knowledge (Nature)" : Skill("int"),
                "Knowledge (Nobility)" : Skill("int"),
                "Knowledge (Planes)" : Skill("int"),
                "Knowledge (Religion)" : Skill("int"),
                "Linguistics" : Skill("int"),
                "Perception" : Skill("wis"),
                "Ride" : Skill("dex"),
                "Sense Motive" : Skill("wis"),
                "Sleight of Hand" : Skill("dex"),
                "Spellcraft" : Skill("int"),
                "Stealth" : Skill("dex"),
                "Survival" : Skill("wis"),
                "Swim" : Skill("str"),
                "Use Magic Device" : Skill("cha")
            },
            "skillRanks" : 0,

            "spells" : {}

        }

    def getStat(self, stat):
        return self.func(stat)

    def getStatMod(self, stat):
        return getModifier(self.func(stat))

    def getName(self):
        return " ".join(self.func("name"))

    def getSize(self):
        return self.func("size")

    def getType(self):
        return self.func("type")

    def getInitBonus(self):
        initStats = self.func("initStats")
        total = 0
        for stat in initStats:
            total += self.getStatMod(stat)
        initBonus = self.func("initBonus")
        return total + initBonus

    def getAC(self):
        natBonus = self.func("naturalACBonus")
        dodgeBonus = self.func("dodgeACBonus")
        deflectBonus = self.func("deflectACBonus")
        miscBonus = self.func("miscACBonus")
        armorBonus = self.func("armorACBonus")
        shieldBonus = self.func("shieldACBonus")
        sizeBonus = getSizeModifier(self.func("size"))
        stats = self.func("ACStats")

        totalStats = 0
        for stat in stats:
            totalStats += getModifier(self.func(stat))

        return 10 + totalStats + natBonus + dodgeBonus + deflectBonus + miscBonus + armorBonus + shieldBonus + sizeBonus

    def getTouchAC(self):
        dodgeBonus = self.func("dodgeACBonus")
        stats = self.func("ACStats")
        sizeBonus = getSizeModifier(self.func("size"))

        totalStats = 0
        for stat in stats:
            totalStats += getModifier(self.func(stat))

        return 10 + totalStats + dodgeBonus + sizeBonus

    def getFlatAC(self):
        natBonus = self.func("naturalACBonus")
        deflectBonus = self.func("deflectACBonus")
        miscBonus = self.func("miscACBonus")
        armorBonus = self.func("armorACBonus")
        shieldBonus = self.func("shieldACBonus")

        ac = 10 + natBonus + deflectBonus + miscBonus + armorBonus + shieldBonus

        # if our modifier is negative, it still applies
        stats = self.func("ACStats")
        totalStats = 0
        for stat in stats:
            totalStats += getModifier(self.func(stat))
        if totalStats < 0:
            ac += totalStats

        sizeBonus = getSizeModifier(self.func("size"))
        if sizeBonus < 0:
            ac += sizeBonus

        return ac

    def getExtraHP(self):
        lvl = self.func("lvl")
        hpStats = self.func("hpStats")

        total = 0
        for stat in hpStats:
            total += self.getStatMod(stat)
        return total * lvl

    def getAverageHP(self):
        hd = self.func("hd");
        hdAverage = self.getExtraHP()
        for i in hd:
            hdAverage += (i[0] * (i[1] / 2))
        return math.floor(hdAverage)

    def getHDString(self):
        hd = self.func("hd");
        hpExtra = self.getExtraHP()
        return getDiceSetString(hd, hpExtra)

    def getFortSave(self):
        bonus = self.func("fortSaveBonus")
        fortSaveStats = self.func("fortSaveStats")
        total = 0
        for stat in fortSaveStats:
            total += self.getStatMod(stat)

        return bonus + total

    def getRefSave(self):
        bonus = self.func("refSaveBonus")
        refSaveStats = self.func("refSaveStats")
        total = 0
        for stat in refSaveStats:
            total += self.getStatMod(stat)

        return bonus + total

    def getWillSave(self):
        bonus = self.func("willSaveBonus")
        willSaveStats = self.func("willSaveStats")
        total = 0
        for stat in willSaveStats:
            total += self.getStatMod(stat)

        return bonus + total

    def getSpeed(self):
        return self.func("speed")

    def getMeleeAttacks(self):
        return self.func("melee")

    def getRangedAttacks(self):
        return self.func("ranged")

    def getSpellLists(self):
        return self.func("spells")

    def getBAB(self):
        return self.func("BAB")

    # Get AC, CMD, and CMB
    def getCMB(self):
        stats = self.func("CMBStats")

        total = 0
        for stat in stats:
            total += self.getStatMod(stat)

        return self.getBAB() + total

    def getCMD(self):
        statsStill = self.func("CMDStats1")
        statsMove = self.func("CMDStats2")

        total = 0
        for stat in statsStill:
            total += self.getStatMod(stat)

        return 10 + total + self.getBAB() + self.func("CMDBonus")

    def getFlatCMD(self):
        statsStill = self.func("CMDStats1")
        statsMove = self.func("CMDStats2")

        total = 0
        for stat in statsStill:
            total += self.getStatMod(stat)
        for stat in statsMove:
            total += self.getStatMod(stat)

        return 10 + total + self.getBAB() + self.func("CMDBonus")

    def getSkillList(self):
        skills = self.func("skills")
        return skills.keys()

    def getSkillBonus(self, skillName):
        skills = self.func("skills")
        if not skillName in skills:
            return 0
        skill = skills[skillName]

        bonus = 0
        if skill.ranks > 0 and skill.classSkill:
            bonus += 3
        bonus += skill.ranks
        bonus += self.getStatMod(skill.stat)

        # There are some special bonuses skills get due to size.
        if skillName == "Stealth":
            bonus += getStealthSkillModifierBasedOnSize(self.getSize())

        return bonus

    def getAbilityList(self):
        abilities = self.func("abilities")
        return abilities
