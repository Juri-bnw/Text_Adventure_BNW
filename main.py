import random
import kampfsystem
import map
import gegner
import character

def charakter_auswahl():
    print("Wähle deinen Charakter:")
    print("1) Barbar")
    print("2) Zauberer")
    print("3) Paladin")
    print("4) Schurke")

    wahl = input("> ")

    if wahl == "1":
        return character.Barbar
    elif wahl == "2":
        return character.Zauberer
    elif wahl == "3":
        return character.Paladin
    elif wahl == "4":
        return character.Schurke
    else:
        print("Ungültige Auswahl.")
        return charakter_auswahl()

def spiel_start():
    print("Willkommen zum Text Adventure\n")

    spieler = charakter_auswahl()
    print(f"\nDu hast {spieler.name} gewählt.\n")

    spiel_loop(spieler)

def spiel_loop(spieler):
    while True:
        aktion = map.map_loop(spieler)
        ergebnis = map.fuehre_aktion_aus(aktion, spieler)

        if ergebnis is None:
            continue  # keine Aktion nötig

        if isinstance(ergebnis, tuple) and ergebnis[0] == "kampf":
            gegner = ergebnis[1]
            kampfsystem.kampf(spieler, gegner)

spiel_start()
