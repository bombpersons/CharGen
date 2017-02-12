import GUI.Application as guiApp
import GUI.tkGUI.Window as tkWindow

import CharGen.Rulesets.Pathfinder.BaseTemplate as BaseTemplate
import CharGen.Rulesets.Pathfinder.Races.Goblin as Goblin
import CharGen.Rulesets.Pathfinder.Classes.Warrior as Warrior

import CharGen.Rulesets.Pathfinder.Meta as pfRules

if __name__ == "__main__":
    app = guiApp.Application(tkWindow.CharacterGUI, pfRules.get())
    characterId = app.getCharacterManager().createCharacter()
    character = app.getCharacterManager().getCharacter(characterId)
    character.apply(BaseTemplate.BaseTemplate("Bob"))
    character.apply(Goblin.Goblin())
    character.apply(Warrior.Warrior(10))
    app.run()
