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
    noun("Romance", "Romances")
]

class randomNoun():
    def __init__(self, force=None):
        self.force = force

    def __str__(self):
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
    verb("Tarnish", "Tarnishing", "Tarnished")
]

class randomVerb():
    def __str__(self):
        return random.choice(verbs).infinitive

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
    "Cromulant"
]

class randomAdjective():
    def __str__(self):
        return random.choice(adjectives)

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
    "Invariably",
    "Occasionally"
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
    "Your"
]

class randomQualifier():
    def __str__(self):
        return random.choice(qualifiers)

questionForms = [
    [randomInterogative(), randomAdjective(), randomNoun()],
    [randomInterogative(), randomNoun()],
    [randomInterogative(), randomVerb()],
    [randomInterogative(), "not"]
]

def getRandomQuestionForm():
    return random.choice(questionForms)

class randomQuestion():
    def __str__(self):
        questionForm = getRandomQuestionForm()
        return resolveForm(questionForm)

answerForms = [
    ["Because", randomNoun(), "are", randomAdjective()],
    ["Because", randomQualifier(), randomNoun(), "are", randomAdjective()],
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
    ["(The)", randomAdjective(), randomNoun()],
    ["(The)", randomNoun(force="singular"), randomNoun()],
    ["(The)", randomNoun(), "of", randomNoun(force="plural")],
    ["(The)", randomAdjective(), randomAdjective(), randomNoun()],
    ["(The)", randomQualifier(), randomAdjective(), randomNoun()]
]

factionSloganForms = [
    [randomQuestion(), "?", randomQuestion(), "?"],
    [randomQuestion(), "?", randomAnswer()],
    ["We may be", randomAdjective(), "but we're", randomAdjective(), randomNoun(force="plural")],
    [randomVerb(), randomNoun()],
    ["It's", randomQualifier(), randomNoun()],
    ["It's", randomNoun(), "- not", randomNoun()],
    [randomVerb(), "it"],
    ["We're", randomAdjective(), randomNoun(force="plural")],
    ["We're", randomQualifier(), randomNoun(force="plural")],
    ["We're", randomQualifier(), randomAdjective()],
    ["Anything but", randomNoun(), "!"],
    ["Anything but", randomAdjective(), "!"],
    ["Will", randomVerb(), "for", randomNoun()],
    ["Hey", randomNoun(), "-", randomVerb(), "a", randomNoun()]
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
