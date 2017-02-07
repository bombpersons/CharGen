from CharGen.Rulesets.Pathfinder.Rules import *
from CharGen.Rulesets.Pathfinder.BaseTemplate import BaseTemplate
from CharGen.Rulesets.Pathfinder.Races.Goblin import Goblin
from CharGen.Rulesets.Pathfinder.Classes.Warrior import Warrior
from CharGen.Rulesets.Pathfinder.Classes.Wizard import Wizard
from CharGen.Rulesets.Pathfinder.Classes.Sorcerer import Sorcerer

from CharGen.Rulesets.Pathfinder.Weapons import *

from CharGen.Rulesets.Pathfinder.Formatters.DokuWiki import DokuWikiFormatter

# A test template.
class TestTemplate:
    def hd(self, character, total):
        return total + [(2, 6)]

    def naturalACBonus(self, character, total):
        return total + 4

    def melee(self, character, total):
        attack = WesternWeaponList().getRandomWeapon(["Unarmed Attack"]).getAttack(character)
        return total + [attack]

# Main function.
if __name__ == "__main__":
    # Gen a test char and print it.
    character = PathfinderCharacter()

    character.apply(BaseTemplate("Bob"))
    character.apply(Goblin())
    character.apply(TestTemplate())
    character.apply(Warrior(7))

    formatter = DokuWikiFormatter()
    print(formatter.write(character))
