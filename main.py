from CharGen.Rulesets.Pathfinder.Rules import *
import CharGen.Rulesets.Pathfinder.BaseTemplate as BaseTemplate
import CharGen.Rulesets.Pathfinder.Races.Goblin as Goblin
import CharGen.Rulesets.Pathfinder.Classes.Warrior as Warrior
import CharGen.Rulesets.Pathfinder.Classes.Wizard as Wizard
import CharGen.Rulesets.Pathfinder.Classes.Sorcerer as Sorcerer
import CharGen.Rulesets.Pathfinder.Random as Random

from CharGen.Rulesets.Pathfinder.Weapons import *

from CharGen.Rulesets.Pathfinder.Formatters.DokuWiki import DokuWikiFormatter

# A test template.
class TestTemplate:
    def hd(self, character, total):
        return total + [(2, 6)]

    def naturalACBonus(self, character, total):
        return total + 4

    def melee(self, character, total):
        attack = WesternWeaponList().getRandomWeapon(["Simple"]).getAttack(character)
        return total + [attack]

# Main function.
if __name__ == "__main__":
    # Gen a test char and print it.
    character = PathfinderCharacter()

    character.apply(BaseTemplate.BaseTemplate("Bob"))
    character.apply(Random.getRandomRace())
    Random.applyRandomAppropriateClass(character, random.randint(1, 5))

    formatter = DokuWikiFormatter()
    print(formatter.write(character))
