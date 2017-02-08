import re
import random

class Spell:
    def __init__(self, name, lvl, desc, traits):
        self.name = name
        self.lvl = lvl
        self.desc = desc
        self.traits = traits

    def __str__(self):
        s = "Lvl " + str(self.lvl) + " - " + self.name + ": " + self.desc
        if len(self.traits) > 0:
            s += " ("
            i = 0
            for trait in self.traits:
                if i != 0:
                    s += ", "
                s += trait
            s += ")"

        return s

class SpellList:
    def __init__(self):
        self.spells = {}

    def loadFromFile(self, filename):
        # Quick and dirty processing for a list of spells copied from http://paizo.com/pathfinderRPG/prd/indices/spelllists.html
        f = open(filename, 'r')

        # Remove any non-decimal chars from a string.
        non_decimal = re.compile(r'[^\d.]+')

        # Go through each line...
        for line in f:
            columns = line.split("\t")

            # Convert the 3rd, 4th, etc strings into ints.
            spellLevelStr = non_decimal.sub("", columns[0])
            spellLevel = int(spellLevelStr)

            # Name of the spell.
            spellName = columns[1]

            # The school / domain.
            spellTraits = [columns[2]]

            # The description of the spell.
            spellDesc = columns[3]

            # Add a spell.
            self.spells[spellName] = Spell(spellName, spellLevel, spellDesc, spellTraits)

        f.close()

    def getSpell(self, name):
        if name in self.spells:
            return self.spells[name]

    def getRandomSpell(self, lvl, traits=[]):
        potential = []
        for spell in self.spells.values():
            found = True
            for trait in traits:
                if trait not in spell.traits:
                    found = False
            if spell.lvl != lvl:
                found = False

            if found:
                potential += [spell]

        if len(potential) == 0:
            return None

        r = random.randint(0, len(potential) - 1)
        return potential[r]

    def __str__(self):
        s = ""
        for spell in self.spells.values():
            s += str(spell) + "\n"
        return s
