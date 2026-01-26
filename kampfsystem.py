import random

def trifft_angriff(angreifer, verteidiger):
    chance = 70 + (angreifer.dex - verteidiger.dex)                         # Die Grundchance ist 70% (wenn beide gleichviel DEX haben)
    chance = max(10, min(chance, 95))                                       # Hier ist eine kleine Kette von "vergleichen". Kurz gesagt schlechter als 10 und besser als 95 geht es nicht. Nennen wir diese Zahl mal A
    return random.randint(1, 100) <= chance                           # Nun wird eine zufällig gleichverteilt eine Zahl zwischen 1 und 100 gezogen.

def berechne_schaden(angreifer, verteidiger):   # NUR FÜR STANDARDANGRIFF !!! !!!
    basis = angreifer.strenght + random.randint(0, angreifer.strenght // 2)
    schaden = basis - verteidiger.defense
    return max(1, schaden)

def feuerball(angreifer, verteidiger):
    if trifft_angriff(angreifer, verteidiger):
        schaden = 2.00 * angreifer.energy
        angreifer.mana -= 10
        return max(1, schaden)

def standard_angriff(angreifer, verteidiger):
    if trifft_angriff(angreifer, verteidiger):
        schaden = berechne_schaden(angreifer, verteidiger)
        verteidiger.hp -= schaden
        print(f"{angreifer.name} trifft {verteidiger.name} für {schaden} Schaden!")
    else:
        print(f"{angreifer.name} verfehlt!")

def angriffsmenue(spieler, gegner):
    while True:
        print("\nAngriff wählen:\n1) Standardangriff\n2) Zurück")
        wahl = input("> ")

        if wahl == "1":
            standard_angriff(spieler, gegner)
            return True  # Aktion verbraucht Runde

        elif wahl == "2":
            return False  # zurück ins Hauptmenü

        else:
            print("Ungültige Eingabe.")

def gegenstaende_menue(spieler):
    print("\nGegenstände:\nNoch keine Gegenstände vorhanden.")
    input("Weiter...")
    return False

def gegenstaende_menue(spieler):
    print("\nGegenstände:")
    print("Noch keine Gegenstände vorhanden.")
    input("Weiter...")
    return False

def gegner_zug(gegner, spieler):
    print(f"{gegner.name} greift an!")
    standard_angriff(gegner, spieler)

def fliehen(spieler, gegner):
    chance = 50 + (spieler.dex - gegner.dex)
    chance = max(10, min(chance, 90))

    if random.randint(1, 100) <= chance:
        print(f"{spieler.name} konnte fliehen!")
        return True
    else:
        print(f"{spieler.name} konnte nicht fliehen!")
        return False

def kampf(spieler, gegner):
    print(f"\n {spieler.name} vs {gegner.name} ")

    while spieler.hp > 0 and gegner.hp > 0:
        print(f"\n{spieler.name} HP: {spieler.hp} | Mana: {spieler.mana}")
        print(f"{gegner.name} HP: {gegner.hp}")

        print("\nAktion wählen:")
        print("1) Angriff")
        print("2) Gegenstände")
        print("3) Fliehen")

        wahl = input("> ")

        runde_verbraucht = False

        if wahl == "1":
            runde_verbraucht = angriffsmenue(spieler, gegner)

        elif wahl == "2":
            runde_verbraucht = gegenstaende_menue(spieler)

        elif wahl == "3":
            if fliehen(spieler, gegner):
                return
            runde_verbraucht = True

        else:
            print("Ungültige Eingabe.")
            continue

        if gegner.hp <= 0:
            print(f"{gegner.name} wurde besiegt!")
            spieler.exp += gegner.exp_give
            print(f"{spieler.name} erhält {gegner.exp_give} EXP.")
            return

        if runde_verbraucht:
            gegner_zug(gegner, spieler)

        if spieler.hp <= 0:
            print(f"{spieler.name} wurde besiegt...")
            return
