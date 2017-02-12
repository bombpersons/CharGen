from CharGen.Rulesets.Pathfinder.Rules import *
import CharGen.Rulesets.Pathfinder.BaseTemplate as BaseTemplate
import CharGen.Rulesets.Pathfinder.Random as Random
import CharGen.Rulesets.Pathfinder.Races.Grippli as Grippli

from CharGen.Rulesets.Pathfinder.Formatters.DokuWiki import DokuWikiFormatter

import random

class Pirate:
    def __init__(self):
        pass

    def str(self, character, total):
        return min(total + 4, 18)

    def dex(self, character, total):
        return min(total + 4, 18)

# Main function.
if __name__ == "__main__":
    # Generate a character that might be in a tavern.
    character = PathfinderCharacter()

    # Apply random base stats.
    character.apply(BaseTemplate.BaseTemplate(""))

    # Apply Pirate
    character.apply(Pirate())

    # Apply grippli as a race.
    character.apply(Grippli.Grippli())

    # Give them a random class
    Random.applyRandomAppropriateClass(character, random.randint(2, 3))

    # Print it to the screen.
    formatter = DokuWikiFormatter()
    print(formatter.write(character))
