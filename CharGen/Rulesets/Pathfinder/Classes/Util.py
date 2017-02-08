import CharGen.Rulesets.Pathfinder.Classes.Sorcerer as Sorcerer
import CharGen.Rulesets.Pathfinder.Classes.Wizard as Wizard
import CharGen.Rulesets.Pathfinder.Classes.Warrior as Warrior
import CharGen.Rulesets.Pathfinder.Classes.Commoner as Commoner

import random

def GetRandomAppropriateClass(character, lvl):
    # Classes, with a list of minimum stats
    possibleClasses = {
        #Sorcerer.RandomSorcerer : ["cha"],
        Wizard.WizardRandom : [0, 0, 0, 11, 0, 0],
        Warrior.RandomWarrior : [12, 10, 10, 0, 0, 0]
    }

    commonerClasses = [
        Commoner.Commoner
    ]

    # Get the character stats
    charStats = [
        character.getStat("str"),
        character.getStat("dex"),
        character.getStat("con"),
        character.getStat("int"),
        character.getStat("wis"),
        character.getStat("cha")
    ]

    # Figure out the best class for them.
    shortList = []
    for c, stats in possibleClasses.items():
        qualify = True
        for charStat, stat in list(zip(charStats, stats)):
            if charStat < stat:
                qualify = False

        if qualify:
            shortList += [c]

    # If the character is really crap and doesn't qualify for any of the classes,
    # just give them a commoner class.
    if len(shortList) == 0:
        shortList = commonerClasses

    # Pick one of the shortlist classes at random.
    picked = shortList[random.randint(0, len(shortList) - 1)]
    return picked(lvl)
