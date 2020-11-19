from inheritance.inheritanceUnits import Units

class Soldiers(Units):
    def __init__(self, ident, team):
        Units.__init__(self, ident, team)
    def follow(self, hero):
        pass
