import copy

# Full character is simply a list of templates to apply upon each other.
class Character:
    def __init__(self):
        self.templates = []
        self.defaults = {}

    def apply(self, template):
        self.templates.append(template)

    def func(self, funcName):
        total = copy.deepcopy(self.defaults[funcName])
        for t in self.templates:
            f = getattr(t, funcName, None)
            if f:
                total = f(self, total)
        return total

    def __str__(self):
        s = "";
        for key in self.defaults:
            s += key + ": " + str(self.func(key)) + "\n"
        return s
