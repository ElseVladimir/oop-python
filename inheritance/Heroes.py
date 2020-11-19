from inheritance.inheritanceUnits import Units

class Heroes(Units):
    def __init__(self, ident, team, level):
        Units.__init__(self, ident, team)
        self.level = level
    def levelup(self):
        self.level += 1