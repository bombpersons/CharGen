import CharGen.Dice as Dice
from CharGen.Character import *

# Ability scores.
class AbilityScores:
    def __init__(self):
        self.str = 10
        self.dex = 10
        self.con = 10
        self.int = 10
        self.wis = 10
        self.cha = 10

    def randomize(self):
        self.str = Dice.rollDice(3, 6)
        self.dex = Dice.rollDice(3, 6)
        self.con = Dice.rollDice(3, 6)
        self.int = Dice.rollDice(3, 6)
        self.wis = Dice.rollDice(3, 6)
        self.cha = Dice.rollDice(3, 6)

# Base template for a character.
class BaseCharacter:
    def __init__(self, name):
        self.abilityScores = AbilityScores();
        self.abilityScores.randomize()

        self.charName = name

    def str(self, character, total):
        return self.abilityScores.str
    def dex(self, character, total):
        return self.abilityScores.dex
    def con(self, character, total):
        return self.abilityScores.con
    def int(self, character, total):
        return self.abilityScores.int
    def wis(self, character, total):
        return self.abilityScores.wis
    def cha(self, character, total):
        return self.abilityScores.cha

    def name(self, character, total):
        return [self.charName]

    def init(self, character, total):
        return getModifier(character.func("dex"))

    def fortSave(self, character, total):
        return getModifier(character.func("con"))
    def refSave(self, character, total):
        return getModifier(character.func("dex"))
    def willSave(self, character, total):
        return getModifier(character.func("wis"))
