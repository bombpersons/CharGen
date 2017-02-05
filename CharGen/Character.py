import CharGen.Dice as Dice

import math
from enum import Enum

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

# Vision for characters.
class Vision(Enum):
    NORMAL=1
    LOW_LIGHT=2
    DARK=3

def getModifier(score):
    normalised = score - 10
    return math.floor(normalised / 2)

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

            "size" : Size.MEDIUM,

            "name" : [],
            "vision" : [],

            "init" : 0,

            "hpExtra" : 0,
            "hd" : [],

            "lvl" : 0,

            "fortSave" : 0,
            "refSave" : 0,
            "willSave" : 0,

            "BAB" : 0,
            "CMB" : 0,
            "CMD" : 0,

            "melee" : [],
            "ranged" : [],
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
