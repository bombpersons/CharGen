import CharGen.Dice as Dice

import math
from enum import Enum

# useful function to convert an integer like 3 to +3
def intToBonusString(n, includeZero=True, before="", after=""):
    if n < 0:
        return before + "-" + after + str(abs(n))
    elif n > 0:
        return before + "+" + after + str(n)
    else:
        return str(n) if includeZero else ""

# Sizes for characters.
class Size(Enum):
    SMALL=1
    MEDIUM=2

def speedFromSize(size):
    if size == Size.SMALL:
        return 20
    elif size == Size.MEDIUM:
        return 30

def getSizeModifier(size):
    if size == Size.SMALL:
        return 1
    elif size == Size.MEDIUM:
        return 0

def getSizeSkillModifier(size):
    if size == Size.SMALL:
        return 4
    elif size == Size.MEDIUM:
        return 0

def getSizeString(size):
    if size == Size.SMALL:
        return "Small"
    elif size == Size.MEDIUM:
        return "Medium"

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

# Functions for dealing with HD
def getExtraHP(character):
    lvl = character.func("lvl")
    hpStats = character.func("hpStats")

    total = 0
    for stat in hpStats:
        total += getModifier(character.func(stat))
    return total * lvl

def getAverageHP(character):
    hd = character.func("hd");
    hpExtra = getExtraHP(character)

    hdAverage = hpExtra
    for i in hd:
        hdAverage += (i[0] * (i[1] / 2))
    return math.floor(hdAverage)

def getDiceString(dice, bonus=0, before="", after=""):
    return str(dice[0]) + "d" + str(dice[1]) + intToBonusString(bonus, includeZero=False, before=before, after=after)

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
        s += intToBonusString(bonus, includeZero=False, before=before, after=after)
    return s

def getHDString(character):
    hd = character.func("hd");
    hpExtra = getExtraHP(character)
    return getDiceSetString(hd, hpExtra)

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
        s = self.name + " " + intToBonusString(self.getToHit()) + " "
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

# Get AC, CMD, and CMB
def getCMB(character):
    stats = character.func("CMBStats")

    total = 0
    for stat in stats:
        total += getModifier(character.func(stat))

    return character.func("BAB") + total

def getCMD(character, flat=False):
    statsStill = character.func("CMDStats1")
    statsMove = character.func("CMDStats2")

    total = 0
    for stat in statsStill:
        total += getModifier(character.func(stat))
    if not flat:
        for stat in statsMove:
            total += getModifier(character.func(stat))

    return 10 + total + character.func("BAB") + character.func("CMDBonus")

def getAC(character):
    natBonus = character.func("naturalACBonus")
    dodgeBonus = character.func("dodgeACBonus")
    deflectBonus = character.func("deflectACBonus")
    miscBonus = character.func("miscACBonus")
    armorBonus = character.func("armorACBonus")
    shieldBonus = character.func("shieldACBonus")
    stats = character.func("ACStats")

    totalStats = 0
    for stat in stats:
        totalStats += getModifier(character.func(stat))

    return 10 + totalStats + natBonus + dodgeBonus + deflectBonus + miscBonus + armorBonus + shieldBonus

def getTouchAC(character):
    dodgeBonus = character.func("dodgeACBonus")
    stats = character.func("ACStats")
    sizeBonus = getSizeModifier(character.func("size"))

    totalStats = 0
    for stat in stats:
        totalStats += getModifier(character.func(stat))

    return 10 + totalStats + dodgeBonus + sizeBonus

def getFlatAC(character):
    natBonus = character.func("naturalACBonus")
    deflectBonus = character.func("deflectACBonus")
    miscBonus = character.func("miscACBonus")
    armorBonus = character.func("armorACBonus")
    shieldBonus = character.func("shieldACBonus")

    ac = 10 + natBonus + deflectBonus + miscBonus + armorBonus + shieldBonus

    # if our modifier is negative, it still applies
    stats = character.func("ACStats")
    totalStats = 0
    for stat in stats:
        totalStats += getModifier(character.func(stat))
    if totalStats < 0:
        ac += totalStats

    sizeBonus = getSizeModifier(character.func("size"))
    if sizeBonus < 0:
        ac += sizeBonus

    return ac

# skills
class Skill:
    def __init__(self, stat):
        self.stat = stat
        self.ranks = 0
        self.classSkill = False

def getSkillBonus(character, skillName):
    skills = character.func("skills")
    if not skillName in skills:
        return 0
    skill = skills[skillName]

    bonus = 0
    if skill.ranks > 0 and skill.classSkill:
        bonus += 3
    bonus += skill.ranks
    bonus += getModifier(character.func(skill.stat))

    # There are some special bonuses skills get due to size.
    if skillName == "Stealth":
        bonus += getSizeSkillModifier(character.func("size"))

    return bonus

# special abilities
class Ability:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

# Full character is simply a list of templates to apply upon each other.
class Character:
    def __init__(self):
        self.templates = []

        self.defaults = {
            "str" : 0,
            "dex" : 0,
            "con" : 0,
            "int" : 0,
            "wis" : 0,
            "cha" : 0,

            "sex" : Sex.MALE,
            "type" : "Humanoid",
            "size" : Size.MEDIUM,
            "speed" : 0,

            "name" : [],
            "vision" : [],

            "init" : 0,

            "hd" : [],
            "hpStats" : ["con"],

            "lvl" : 0,

            "naturalACBonus" : 0,
            "dodgeACBonus" : 0,
            "deflectACBonus" : 0,
            "miscACBonus" : 0,
            "armorACBonus" : 0,
            "shieldACBonus" : 0,
            "ACStats" : ["dex"],

            "fortSave" : 0,
            "refSave" : 0,
            "willSave" : 0,

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
            }
        }

    def apply(self, template):
        self.templates.append(template)

    def func(self, funcName):
        total = self.defaults[funcName]
        for t in self.templates:
            f = getattr(t, funcName, None)
            if f:
                total = f(self, total)
        return total

    def __str__(self):
        s = "";
        for key in self.defaults:
            s += key + ": " + str(self.func(key)) + "\n"
        return s
