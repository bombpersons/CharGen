from CharGen.Rulesets.Pathfinder.Rules import *
from CharGen.Rulesets.Pathfinder.BaseCharacter import BaseCharacter
from CharGen.Rulesets.Pathfinder.Races.Goblin import Goblin
from CharGen.Rulesets.Pathfinder.Classes.Warrior import Warrior
from CharGen.Rulesets.Pathfinder.Classes.Wizard import Wizard
from CharGen.Rulesets.Pathfinder.Classes.Sorcerer import Sorcerer

from CharGen.Rulesets.Pathfinder.Formatters.DokuWiki import DokuWikiFormatter

# A test template.
class TestTemplate:
    def hd(self, character, total):
        return total + [(2, 6)]

    def naturalACBonus(self, character, total):
        return total + 4

    def melee(self, character, total):
        attack = Attack(character)
        attack.dmgDice = (2, 6)
        attack.dmgStat = "str"
        attack.toHitStat = "str"
        attack.name = "Magic Ice Great Sword"
        attack.twoHanded = True

        attack.dmgExtraDice = (1, 6)
        attack.dmgExtraType = "ice"

        attack2 = Attack(character)
        attack2.dmgDice = (1, 6)
        attack2.dmgStat = "str"
        attack2.toHitStat = "dex"
        attack2.name = "Rapier"
        attack2.twoHanded = False

        return total + [attack, attack2]

    def ranged(self, character, total):
        attack = Attack(character)
        attack.dmgDice = (1, 6)
        attack.dmgStat = ""
        attack.toHitStat = "dex"

        attack.enhancement = 2
        attack.masterwork = True

        attack.name = "+2 Shortbow"
        attack.twoHanded = True

        return total + [attack]

# Main function.
if __name__ == "__main__":
    # Gen a test char and print it.
    character = PathfinderCharacter()

    character.apply(BaseCharacter("Bob"))
    character.apply(Goblin())
    character.apply(TestTemplate())
    character.apply(Warrior(7))
    character.apply(Wizard(3))
    character.apply(Sorcerer(10))

    formatter = DokuWikiFormatter()
    print(formatter.write(character))
