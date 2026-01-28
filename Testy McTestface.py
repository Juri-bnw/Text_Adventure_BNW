
#______________________________________________________________ MUSS GEÄNDERT WERDEN
def naechste_aktion(spieler):
    print("\n Was möchtest du als Nächstes tun?")
    print("1) Wald erkunden")
    print("2) Stadt erkunden")
    print("3) Dungeon erkunden")

    input()

def wald_erkunden(spieler):
    print("\nDu gehst weiter...")
    input()

    ereignis = random.randint(1, 100)

    if ereignis <= 50:
        print("Ein Gegner taucht auf !!!")
        return "kampf"



def rasten(spieler):
    hp_heilung = int(spieler.max_HP * 0.1)

    spieler.current_HP += hp_heilung
    if spieler.current_HP > spieler.max_HP:
        spieler.current_HP = spieler.max_HP
        hp_heilung = 0
        print(f"Du bist vollständig geheilt und hast im Moment {spieler.current_HP} / {spieler.max_HP} HP")
    else: print(f"Du rastest und erhältst {hp_heilung} HP. Im Moment hast du {spieler.current_HP} / {spieler.max_HP} HP.")












import random

def trifft_angriff(angreifer, verteidiger):
    chance = 70 + (angreifer.dex - verteidiger.dex)
    chance = max(20, min(chance, 90))
    return random.randint(1, 100) <= chance

def berechne_schaden(angreifer, verteidiger):
    basis = angreifer.strength + random.randint(0, angreifer.strength // 2)
    schaden = basis - verteidiger.defense
    return max(1, schaden)

def standard_angriff(angreifer, verteidiger):
    if trifft_angriff(angreifer, verteidiger):
        schaden = berechne_schaden(angreifer, verteidiger)
        verteidiger.current_HP -= schaden
        verteidiger.current_HP = max(0, verteidiger.current_HP)
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
    spieler.current_mana = spieler.max_mana
    print(f"\n {spieler.name} vs {gegner.name} ")
    while spieler.current_HP > 0 and gegner.current_HP > 0:
        print(f"\n{spieler.name} HP: {spieler.current_HP} | Mana: {spieler.current_mana}")
        print(f"{gegner.name} HP: {gegner.current_HP}")

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

        if gegner.current_HP <= 0:
            print(f"{gegner.name} wurde besiegt!")
            spieler.exp += gegner.exp_give
            print(f"{spieler.name} erhält {gegner.exp_give} EXP.")
            return

        if runde_verbraucht:
            gegner_zug(gegner, spieler)

            if spieler.current_HP <= 0:
                print(f"{spieler.name} ist besiegt...")
                return
