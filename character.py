class Character:
    def __init__(self, name, level, exp, max_HP, strength, dex, energy, defense, mana, charisma, luck):
        self.name = name
        self.level = level
        self.exp = exp
        self.max_HP = max_HP
        self.current_HP = max_HP
        self.strength = strength
        self.dex = dex
        self.energy = energy
        self.defense = defense
        self.max_mana = mana
        self.current_mana = mana
        self.charisma = charisma
        self.luck = luck

Barbar = Character("Barbar", 1, 0, 1000, 100, 70, 10, 70, 20, 20, 20)
Zauberer = Character("Zauberer", 1, 0, 400, 40, 90, 150, 30, 250, 40, 30)
Paladin = Character("Paladin", 1, 0, 800, 90, 50, 50, 70, 50, 50, 40)
Schurke = Character("Schurke", 1, 0, 600, 70, 120, 30, 50, 50, 20, 100)
