import random as random

class noun:
    def __init__(self, singular, plural):
        self.singular = singular
        self.plural = plural

class verb:
    def __init__(self, present, infinitive, past):
        self.present=present
        self.infinitive=infinitive
        self.past=past

nouns = [
    noun("Witch", "Witches"),
    noun("Fish", "Fish"),
    noun("Dungeon", "Dungeons"),
    noun("Ork", "Orks"),
    noun("Boy", "Boyz"),
    noun("Runt", "Runts"),
    noun("Death", "Deaths"),
    noun("Secret", "Secrets"),
    noun("Cultist", "Cultists"),
    noun("Shoe", "Shoes"),
    noun("Toe", "Toes"),
    noun("Axe", "Axes"),
    noun("Tramp", "Tramps"),
    noun("Truth", "Truths"),
    noun("Lie", "Lies"),
    noun("Friend", "Friends"),
    noun("Problem", "Problems"),
    noun("Doubt", "Doubts"),
    noun("Mother", "Mothers"),
    noun("Father", "Fathers"),
    noun("Man", "Men"),
    noun("Woman", "Women"),
    noun("Ego", "Egos"),
    noun("God", "Gods"),
    noun("Constable", "Constables"),
    noun("Vulture", "Vultures"),
    noun("Dream", "Dreams"),
    noun("Horror", "Horrors"),
    noun("Choice", "Choices"),
    noun("Cabinet", "Cabinets"),
    noun("Problem", "Problems"),
    noun("Solution", "Solution"),
    noun("Eye", "Eyes"),
    noun("Slug", "Slugs"),
    noun("Bargain", "Bargains"),
    noun("Dragon", "Dragons"),
    noun("Romance", "Romances"),
    noun("Dog", "Dogs"),
    noun("Death", "Deaths"),
    noun("Pack", "Packs"),
    noun("Finger", "Fingers"),
    noun("Jelly", "Jellies"),
    noun("Clock", "Clocks"),
    noun("Freak", "Freaks"),
    noun("Priest", "Priests"),
    noun("Insult", "Insults"),
    noun("Dissapointment", "Dissapointments"),
    noun("Harvest", "Harvests"),
    noun("Star", "Stars"),
    noun("Child", "Children"),
    noun("Velociraptor", "Velociraptors"),
    noun("Murder", "Murders"),
    noun("Killer", "Killers"),
    noun("Band", "Bands"),
    noun("Fang", "Fangs"),
    noun("Captor", "Captors"),
    noun("Soldier", "Soldiers"),
    noun("Word", "Words"),
    noun("World", "Worlds")
]

class randomNoun():
    def __init__(self, force=None):
        self.force = force
        self.hyphenPercentage = 7

    def __str__(self):
        if random.randint(1,100) <= self.hyphenPercentage:
            noun1 = randomNoun(force="singular")
            noun2 = randomNoun()
            return str(noun1) + "-" + str(noun2)

        choice = random.choice(nouns)

        if self.force=="singular":
            return choice.singular
        elif self.force=="plural":
            return choice.plural

        choices = [choice.singular, choice.plural]
        return random.choice(choices)

verbs = [
    verb("Shoot", "Shooting", "Shot"),
    verb("Burn", "Burning", "Burnt"),
    verb("Shine", "Shining", "Shone"),
    verb("Strike", "Striking", "Struck"),
    verb("Share", "Sharing", "Shared"),
    verb("Hop", "Hopping", "Hopped"),
    verb("Pop", "Popping", "Popped"),
    verb("Wake", "Waking", "Waked"),
    verb("End", "Ending", "Ended"),
    verb("Die", "Dying", "Deceased"),
    verb("Break", "Breaking", "Broken"),
    verb("Fly", "Flying", "Flew"),
    verb("Kill", "Killing", "Killed"),
    verb("Fool", "Fooling", "Fooled"),
    verb("Tarnish", "Tarnishing", "Tarnished"),
	verb("Eat", "Eating", "Eaten"),
	verb("Love", "Loving", "Loved"),
	verb("Hate", "Hating", "Hate"),
    verb("Fly", "Flying", "Flew"),
    verb("Abandon", "Abandoning", "Abandoned"),
    verb("Grow", "Growing", "Grown"),
    verb("Shrink", "Shrinking", "Shrunken"),
    verb("Rotate", "Rotating", "Rotated"),
    verb("Pickle", "Pickling", "Pickled"),
    verb("Ferment", "Fermenting", "Fermented"),
    verb("Sheath", "Sheathing", "Sheathed"),
    verb("Work", "Working", "Worked"),
    verb("Capture", "Capturing", "Captured"),
    verb("Embarass", "Embarassing", "Embarassed"),
    verb("Twist", "Twisting", "Twisted")
]

class randomVerb():
    def __init__(self,force=None):
        self.force=force

    def __str__(self):
        choices = random.choice(verbs)

        if self.force=="present":
            return choices.present
        if self.force=="infinitive":
            return choices.infinitive
        else:
            return random.choice([choices.infinitive, choices.past])

adjectives = [
    "Runty",
    "Shooty",
    "Tip-top",
    "Super",
    "Ultra",
    "Questionable",
    "Tasteful",
    "Honourable",
    "Still",
    "Smelly",
    "Dirty",
    "Grimy",
    "Wonderous",
    "Slimy",
    "Supspicious",
    "Flexible",
    "Wobbly",
    "Creative",
    "Bogus",
    "Alternative",
    "Actual",
    "Genuine",
    "Faux",
    "Misleading",
    "Not",
    "Niggling",
    "Irksome",
    "Dubious",
    "Witty",
    "Wonky",
    "Pilfered",
    "Concerned",
    "Macho",
    "Effeminate",
    "Elongated",
    "Inflated",
    "Damned",
    "Incredibly",
    "Invariable",
    "Occasional",
    "Dead",
    "Living",
    "Impossible",
    "Personal",
    "First",
    "Foremost",
    "Second",
    "Third",
    "Final",
    "Last",
    "Shit",
    "Bad",
    "Good",
    "Lazy",
    "Mean",
    "Kind",
    "Sick",
    "Misbegotten",
    "Unkind",
    "Simple",
    "Vengeful",
    "Cromulant",
	"Fighty",
    "Fishy",
    "Turbulent",
    "Hot",
    "Cold",
    "Lukewarm",
    "Ticklish",
    "Hungry",
    "Wicked",
    "Elder",
    "Old",
    "Evil",
    "Holy",
    "Bottom",
    "Red",
    "Crimson",
    "Yellow",
    "Blue",
    "Black",
    "White",
    "Dangerous",
    "Carion",
    "Slavering",
    "Scaly"
]

class randomAdjective():
    def __str__(self):
        return random.choice(adjectives)

class randomVerbAdjectiveOrNoun():
    def __str__(self):
        return str(random.choice([randomVerb(force="past"), randomNoun(force="plural"), randomAdjective()]))

interogatives = [
    "Why",
    "When",
    "Where",
    "How",
    "What",
    "Whyfor",
    "Wence",
    "Wherefor",
    "Whither",
]

class randomInterogative():
    def __str__(self):
        return random.choice(interogatives)

qualifiers = [
    "All",
    "No",
    "Some",
    "Invariably",
    "Occasionally",
    "Our",
    "Your",
    "Invariably",
    "Occasionally"
]

class randomQualifier():
    def __str__(self):
        return random.choice(qualifiers)

questionForms = [
    [randomInterogative(), randomAdjective(), randomNoun()],
    [randomInterogative(), randomNoun()],
    [randomInterogative(), randomVerb()],
    [randomInterogative(), "not"],
    ["What do we want"]
]

def getRandomQuestionForm():
    return random.choice(questionForms)

class randomQuestion():
    def __str__(self):
        questionForm = getRandomQuestionForm()
        return resolveForm(questionForm)

answerForms = [
    ["Because", randomNoun(), "are", randomAdjective()],
    ["Because", randomQualifier(), randomNoun(force="plural"), "are", randomAdjective()],
    [randomNoun(), "are", randomNoun()],
    [randomVerb(), randomNoun()]
]

def getRandomAnswerForm():
    return random.choice(answerForms)

class randomAnswer():
    def __str__(self):
        answerForm = getRandomAnswerForm()
        return resolveForm(answerForm)

factionNameForms = [
    ["(The)", randomAdjective(), randomNoun(force="plural")],
    ["(The)", randomNoun(force="singular"), randomNoun(force="plural")],
    ["(The)", randomNoun(), "of", randomNoun(force="plural")],
    ["(The)", randomNoun(), "of", randomVerb(force="infinitive")],
    ["(The)", randomAdjective(), randomAdjective(), randomNoun()],
    ["(The)", randomQualifier(), randomAdjective(), randomNoun()],
    ["(The)", randomQualifier(), randomNoun()]
]

class randomSubject():
    def __str__(self):
        return str(random.choice([randomNoun(force="plural"), str(randomQualifier()) + " " + str(randomNoun())]))

factionSloganForms = [
    ["For", randomNoun()],
    [randomQuestion(), "?", randomQuestion(), "?"],
    [randomQuestion(), "?", randomAnswer()],
    [randomQuestion(), "?", randomNoun(), "!"],
    ["We may be", randomAdjective(), "but we're", randomAdjective(), randomNoun(force="plural")],
    [randomVerb(), randomNoun()],
    ["It's", randomQualifier(), randomNoun()],
    ["It's", randomNoun(), "- not", randomNoun()],
    [randomVerb(), "it"],
    [randomNoun(), "!", randomNoun(), "!", randomNoun(), "!"],
    ["We're", randomAdjective(), randomNoun(force="plural")],
    ["We're", randomQualifier(), randomNoun(force="plural")],
    ["We're", randomQualifier(), randomAdjective()],
    ["Anything but", randomNoun(), "!"],
    ["Anything but", randomAdjective(), "!"],
    ["Will", randomVerb(force="present"), "for", randomNoun()],
    ["Hey", randomNoun(), "-", randomVerb(), "a", randomNoun(force="singular")],
    ["We're", randomVerb(force="infinitive"), randomQualifier(), randomNoun()],
    [randomQualifier(), randomNoun(), randomQualifier(), randomNoun()],
    ["It's", randomAdjective(), "to go alone - here, take", randomNoun(force="plural")],
    ["It's", randomQualifier(), randomAdjective(), randomVerb(force="infinitive"), randomVerbAdjectiveOrNoun()],
    ["You're", randomVerb(force="infinitive"), "my", randomNoun(), ", man."],
    ["We're gonna", randomVerb(force="present"), randomSubject()]
]

def getNoun():
    return random.choice(nouns)

def getVerb():
    return random.choice(verbs)

def getAdjective():
    return random.choice(adjectives)

def getFactionNameForm():
    return random.choice(factionNameForms)

def getFactionSloganForm():
    return random.choice(factionSloganForms)

def getFactionName():
    nameForm = getFactionNameForm()
    return resolveForm(nameForm)

def getFactionSlogan():
    sloganForm = getFactionSloganForm()
    return resolveForm(sloganForm)

def resolveForm(form):
    string = " ".join([str(i) for i in form])
    return string

def getFaction():
    return getFactionName(), getFactionSlogan()


# Main function.
if __name__ == "__main__":
    factionName, factionSlogan = getFaction()
    print(factionName)
    print("\"" + factionSlogan + "\"")
