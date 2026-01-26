import random
import kampfsystem

class Character:
    def __init__(self, name, level, exp, hp, strenght, dex, energy, defense, mana, charisma, luck):
        self.name = name
        self.level = level
        self.exp = exp
        self.hp = hp
        self.strenght = strenght
        self.dex = dex
        self.energy = energy
        self.defense = defense
        self.mana = mana
        self.charisma = charisma
        self.luck = luck

class Gegner:
    def __init__(self, name, level, hp, strenght, dex, energy, defense, exp_give):
        self.name = name
        self.level = level
        self.hp = hp
        self.strenght = strenght
        self.dex = dex
        self.energy = energy
        self.defense = defense
        self.exp_give = exp_give

class Faehigkeiten:
    def __init__(self, name, level, strenght, dex, energy, mana, charisma, luck):
        self.name = name
        self.level = level
        self.strenght = strenght
        self.dex = dex
        self.energy = energy
        self.mana = mana
        self.charisma = charisma
        self.luck = luck

class Gegenstaende:
    def __init__(self, name, bonuses):
        self.name = name
        self.bonuses = bonuses


Barbar = Character("Barbar", 1, 0, 1000, 100, 70, 10, 70, 20, 20, 20 )
Zauberer = Character("Zauberer", 1, 0, 400, 40, 90, 150, 30, 250, 40, 30)
Paladin = Character("Paladin", 1, 0, 800, 90, 50, 50, 70, 50, 50, 40)
Schurke = Character("Schurke", 1, 0, 600, 70, 120, 30, 50, 50, 20, 100)

Skelett = Gegner("Skelett", 1, 50, 10, 15, 0, 0, 10)
Fledermaus = Gegner("Fledermaus", 1, 20, 10, 40, 0, 5, 10)
Ratte = Gegner("Ratte", 1, 20, 20, 20, 0, 10, 10)



kampfsystem.kampf(Schurke, Ratte)