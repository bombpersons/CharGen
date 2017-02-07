import GUI.Application as guiApp
import GUI.tkGUI.Window as tkWindow
import CharGen.Rulesets.Pathfinder.Rules as pfRules

import CharGen.Rulesets.Pathfinder.BaseCharacter as BaseCharacter
import CharGen.Rulesets.Pathfinder.Races.Goblin as Goblin
import CharGen.Rulesets.Pathfinder.Classes.Warrior as Warrior

if __name__ == "__main__":
    app = guiApp.Application(tkWindow.CharacterGUI, pfRules.PathfinderCharacter)
    app.character.apply(BaseCharacter.BaseCharacter("Bob"))
    app.character.apply(Warrior.Warrior(10))
    app.run()
