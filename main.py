from CharGen.Character import Character
from CharGen.BaseCharacter import BaseCharacter
from CharGen.Races.Orc import Orc
from CharGen.Classes.Warrior import Warrior

from CharGen.Formatters.DokuWiki import DokuWikiFormatter

# Main function.
if __name__ == "__main__":
    # Gen a test char and print it.
    character = Character()

    character.apply(BaseCharacter("Bob"))
    character.apply(Orc())
    character.apply(Warrior(7))

    formatter = DokuWikiFormatter()
    print(formatter.write(character))
