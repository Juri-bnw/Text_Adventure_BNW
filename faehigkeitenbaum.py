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
    ziel_anzahl=1
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

Meteor = (Faehigkeit
    (name="Meteor",
     mana_cost=50,
     base_dmg=30,
     scale_energy=0.8,
     ziel_typ="gegner",
     ziel_anzahl="alle"))



