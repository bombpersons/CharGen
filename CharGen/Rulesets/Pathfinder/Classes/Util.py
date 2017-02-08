import CharGen.Rulesets.Pathfinder.Classes.Sorcerer as Sorcerer
import CharGen.Rulesets.Pathfinder.Classes.Wizard as Wizard
import CharGen.Rulesets.Pathfinder.Classes.Warrior as Warrior
import CharGen.Rulesets.Pathfinder.Classes.Commoner as Commoner

import random

def GetRandomAppropriateClass(character, lvl):
    # Classes, with a list of stats that are useful for them.
    possibleClasses = {
        #Sorcerer.RandomSorcerer : ["cha"],
        Wizard.WizardRandom : ["int"],
        #Warrior.RandomWarrior : ["str"]
    }

    commonerClasses = [
        Commoner.Commoner
    ]

    # Figure out the best class for them.
    shortList = []
    for c, stats in possibleClasses.items():
        qualify = False
        for stat in stats:
            if character.getStat(stat) > 14:
                qualify = True

        if qualify:
            shortList += [c]

    # If the character is really crap and doesn't qualify for any of the classes,
    # just give them a commoner class.
    if len(shortList) == 0:
        shortList = commonerClasses

    # Pick one of the shortlist classes at random.
    picked = shortList[random.randint(0, len(shortList) - 1)]
    return picked(lvl)
