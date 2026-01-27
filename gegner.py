class Gegner:
    def __init__(self, name, level, HP, strength, dex, energy, defense, exp_give):
        self.name = name
        self.level = level
        self.max_HP = HP
        self.current_HP = HP
        self.strength = strength
        self.dex = dex
        self.energy = energy
        self.defense = defense
        self.exp_give = exp_give

Skelett = Gegner("Skelett", 1, 50, 10, 15, 0, 0, 10)
Fledermaus = Gegner("Fledermaus", 1, 20, 10, 40, 0, 5, 10)
Ratte = Gegner("Ratte", 1, 20, 20, 20, 0, 10, 10)
Dunkler_Magier = Gegner("Dunkler Magier", 1, 200,10,40,100, 10, 50)