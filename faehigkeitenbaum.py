class Faehigkeit:
    def __init__(
            self,
            name,
            mana_cost,
            base_dmg=0,
            scale_strength=0.0,
            scale_dex=0.0,
            scale_energy=0.0,
            scale_charisma=0.0,
            scale_luck=0.0,
            ziel_typ="gegner",
            ziel_anzahl=1
    ):
        self.name = name
        self.mana_cost = mana_cost
        self.base_dmg = base_dmg
        self.scale_strength = scale_strength
        self.scale_dex = scale_dex
        self.scale_energy = scale_energy
        self.scale_charisma = scale_charisma
        self.scale_luck = scale_luck
        self.ziel_typ = ziel_typ
        self.ziel_anzahl = ziel_anzahl

Feuerball = Faehigkeit(
    name="Feuerball",
    mana_cost=20,
    base_dmg=25,
    scale_energy=0.6,
    ziel_typ="gegner",
    ziel_anzahl=2
)

Blitzschwung = Faehigkeit(
    name="Blitzschwung",
    mana_cost=10,
    base_dmg=10,
    scale_strength=0.6,
    scale_dex=0.2,
    scale_energy=0.1,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)

Meteor = Faehigkeit(
    name="Meteor",
    mana_cost=50,
    base_dmg=30,
    scale_energy=0.8,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)

#Neue Fähigkeiten
Frostnova = Faehigkeit(
    name="Frostnova",
    mana_cost=30,
    base_dmg=15,
    scale_energy=0.4,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)

Wütender_Schlag = Faehigkeit(
    name="Wütender Schlag",
    mana_cost=15,
    base_dmg=20,
    scale_strength=0.8,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)

Erdbeben = Faehigkeit(
    name="Erdbeben",
    mana_cost=40,
    base_dmg=25,
    scale_strength=0.5,
    scale_luck=0.3,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)

Heiliges_Licht = Faehigkeit(
    name="Heiliges Licht",
    mana_cost=25,
    base_dmg=40,
    scale_charisma=0.7,
    ziel_typ="spieler",
    ziel_anzahl="alle"
)

Gerechter_Zorn = Faehigkeit(
    name="Gerechter Zorn",
    mana_cost=20,
    base_dmg=15,
    scale_strength=0.4,
    scale_charisma=0.4,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)

Schildstoss = Faehigkeit(
    name="Schildstoss",
    mana_cost=15,
    base_dmg=10,
    scale_strength=0.3,
    scale_energy=0.3,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)

Meuchelmord = Faehigkeit(
    name="Meuchelmord",
    mana_cost=30,
    base_dmg=50,
    scale_dex=1.0,
    scale_luck=0.5,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)

Giftpfeil = Faehigkeit(
    name="Giftpfeil",
    mana_cost=15,
    base_dmg=20,
    scale_dex=0.6,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)

Klingensturm = Faehigkeit(
    name="Klingensturm",
    mana_cost=40,
    base_dmg=15,
    scale_dex=0.7,
    ziel_typ="gegner",
    ziel_anzahl="alle"
)
