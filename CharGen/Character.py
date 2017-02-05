import CharGen.Dice as Dice

import math
from enum import Enum

# Sizes for characters.
class Size(Enum):
    SMALL=1
    MEDIUM=2

def speedFromSize(size):
    if size == SMALL:
        return 20
    elif size == MEDIUM:
        return 30

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
            "name" : [],
            "vision" : [],
            "init" : 0
        }

    def apply(self, template):
        self.templates.append(template)

    def func(self, funcName):
        total = self.defaults[funcName]
        for t in self.templates:
            f = getattr(t, funcName, self.defaults[funcName])
            if f:
                total += f(self)
        return total

    def __str__(self):
        s = str(self.func("name")) + "\n"
        s += "Ability Scores: "
        s += "Str (" + str(self.func("str")) + "), "
        s += "Dex (" + str(self.func("dex")) + "), "
        s += "Con (" + str(self.func("con")) + "), "
        s += "Int (" + str(self.func("int")) + "), "
        s += "Wis (" + str(self.func("wis")) + "), "
        s += "Cha (" + str(self.func("cha")) + ")\n"

        s += "Vision: " + str(self.func("vision")) + "\n"

        s += "Init " + str(self.func("init"))
        return s
