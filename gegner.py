from ctypes.wintypes import tagRECT
import map


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


Fledermaus = Gegner("Fledermaus", 1, 20, 10, 25, 0, 5, 10)

Schleim = Gegner("Schleim", 1, 20, 15, 20, 0, 15, 10)

Skelett = Gegner("Skelett", 1, 50, 10, 15, 0, 1, 10)

Spinne = Gegner("Spinne", 1, 30, 15, 20, 0, 15, 10)

Zombie = Gegner("Zombie", 1, 50, 15, 10, 0, 10, 10)

Assassine = Gegner("Assassine", 1, 25, 10, 70, 0, 15, 15)

Bandit = Gegner("Bandit", 1, 50, 20, 15, 0, 20, 15)

Goblin = Gegner("Goblin", 1, 40, 30, 10, 0, 20, 15)

Schlange = Gegner("Schlange", 1, 25, 10, 50, 0, 15, 15)

Geist = Gegner("Geist", 1, 50, 10, 40, 0, 30, 20)

Ratte = Gegner("Ratte", 1, 20, 20, 20, 0, 10, 20)

Soldat = Gegner("Soldat", 1, 50, 30, 15, 0, 50, 20)

Wolf = Gegner("Wolf", 1, 50, 30, 30, 0, 25, 20)

Dunkler_Magier = Gegner("Dunkler Magier", 1, 200, 10, 40, 100, 10, 50)

Alien = Gegner("Alien", 1, 500, 30, 50, 50, 25, 100)

Ork = Gegner("Ork", 25, 5000, 1000, 60, 50, 80, 850)

Drache = Gegner("Drache", 50, 10000, 1500, 100, 100, 100, 1650)

Daemon = Gegner("Dämon", 80, 15000, 2000, 200, 150, 200, 2500)
