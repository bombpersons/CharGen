import CharGen.Rulesets.Microlite20.Rules as Rules
import CharGen.Rulesets.Microlite20.Base as Base

import CharGen.Rulesets.Microlite20.Races as Races
import CharGen.Rulesets.Microlite20.Classes as Classes

import CharGen.Rulesets.Microlite20.Random as Random

import CharGen.Rulesets.Microlite20.Formatters as Formatters

if __name__ == "__main__":
    character = Rules.Microlite20Character()

    base = Base.Base()
    base.randomize()

    character.apply(base)
    character.apply(Races.Human())
    Random.applyRandomAppropriate(character, 3)

    print(Formatters.WriteSimple(character))
