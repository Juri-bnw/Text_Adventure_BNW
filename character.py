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
        self.faehigkeiten = []
        self.gold = 100
        self.inventar = []

    def exp_fuer_naechstes_level(self):
        return 100 * self.level

    def erhalte_exp(self, menge):
        self.exp += menge
        print(f"{self.name} erhält {menge} EP!\n")

        while self.exp >= self.exp_fuer_naechstes_level():
            self.exp -= self.exp_fuer_naechstes_level()
            self.level_up()

    def level_up(self):
        self.level += 1
        print(f"LEVEL UP! {self.name} ist jetzt Level {self.level}\n")

        self.max_HP += 50
        self.strength += 5
        self.defense += 4
        self.max_mana += 20

        self.current_HP = self.max_HP
        self.current_mana = self.max_mana


Barbar = Character("Barbar", 1, 0, 1000, 100, 70, 10, 70, 200, 20, 20)
Zauberer = Character("Zauberer", 1, 0, 400, 40, 90, 150, 30, 500, 40, 30)
Paladin = Character("Paladin", 1, 0, 800, 90, 50, 50, 70, 200, 50, 40)
Schurke = Character("Schurke", 1, 0, 600, 70, 120, 30, 50, 200, 20, 100)

from faehigkeitenbaum import (
    Feuerball, Meteor, Frostnova,
    Blitzschwung, Wütender_Schlag, Erdbeben,
    Heiliges_Licht, Gerechter_Zorn, Schildstoss,
    Meuchelmord, Giftpfeil, Klingensturm
)

Zauberer.faehigkeiten = [Feuerball, Meteor, Frostnova]
Barbar.faehigkeiten = [Blitzschwung, Wütender_Schlag, Erdbeben]
Paladin.faehigkeiten = [Heiliges_Licht, Gerechter_Zorn, Schildstoss]
Schurke.faehigkeiten = [Meuchelmord, Giftpfeil, Klingensturm]
