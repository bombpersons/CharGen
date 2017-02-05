from CharGen.Character import Character
from CharGen.BaseCharacter import BaseCharacter
from CharGen.Races.Orc import Orc

# Main function.
if __name__ == "__main__":
    # Gen a test char and print it.
    character = Character()

    character.apply(BaseCharacter("Bob"))
    character.apply(Orc())

    print(character)
