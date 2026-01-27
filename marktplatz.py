import character


def zeige_marktplatz(spieler):
    while True:
        print(f"\n--- MARKTPLATZ (Gold: {spieler.gold}) ---")
        print("1) Gasthaus (Essen & Heilung)")
        print("2) Alchemist (Energie & Tränke)")
        print("3) Trainer (Erfahrung & Training)")
        print("4) Schmied (Waffen & Ausrüstung)")
        print("5) Verlassen")

        wahl = input("> ")

        if wahl == "1":
            gasthaus(spieler)
        elif wahl == "2":
            alchemist(spieler)
        elif wahl == "3":
            trainer(spieler)
        elif wahl == "4":
            schmied(spieler)
        elif wahl == "5":
            break
        else:
            print("Ungültige Auswahl.")


def gasthaus(spieler):
    print("\n--- GASTHAUS ---")
    print("1) Brot (10 Gold) - Heilt 50 HP")
    print("2) Steak (25 Gold) - Heilt 150 HP")
    print("3) Zurück")
    wahl = input("> ")
    if wahl == "1" and spieler.gold >= 10:
        spieler.gold -= 10
        spieler.current_HP = min(spieler.max_HP, spieler.current_HP + 50)
        print("Lecker! Du fühlst dich besser.")
    elif wahl == "2" and spieler.gold >= 25:
        spieler.gold -= 25
        spieler.current_HP = min(spieler.max_HP, spieler.current_HP + 150)
        print("Das war ein Festmahl!")
    elif wahl == "3":
        return
    else:
        print("Nicht genug Gold oder ungültige Wahl.")


def alchemist(spieler):
    print("\n--- ALCHEMIST ---")
    print("1) Manatrank (20 Gold) - Stellt 50 Mana wieder her")
    print("2) Energie-Elixier (50 Gold) - +5 Energie permanent")
    print("3) Zurück")
    wahl = input("> ")
    if wahl == "1" and spieler.gold >= 20:
        spieler.gold -= 20
        spieler.current_mana = min(spieler.max_mana, spieler.current_mana + 50)
        print("Deine magische Energie kehrt zurück.")
    elif wahl == "2" and spieler.gold >= 50:
        spieler.gold -= 50
        spieler.energy += 5
        print("Du fühlst dich energiegeladener!")
    elif wahl == "3":
        return
    else:
        print("Nicht genug Gold oder ungültige Wahl.")


def trainer(spieler):
    print("\n--- TRAINER ---")
    print("1) Kleines Training (40 Gold) - +100 XP")
    print("2) Intensives Training (100 Gold) - +300 XP")
    print("3) Zurück")
    wahl = input("> ")
    if wahl == "1" and spieler.gold >= 40:
        spieler.gold -= 40
        spieler.exp += 100
        print("Du hast etwas gelernt!")
    elif wahl == "2" and spieler.gold >= 100:
        spieler.gold -= 100
        spieler.exp += 300
        print("Du bist deutlich stärker geworden!")
    elif wahl == "3":
        return
    else:
        print("Nicht genug Gold oder ungültige Wahl.")


def schmied(spieler):
    print("\n--- SCHMIED ---")
    print("1) Eisenschwert (60 Gold) - +10 Stärke")
    print("2) Lederrüstung (50 Gold) - +5 Verteidigung")
    print("3) Zurück")
    wahl = input("> ")
    if wahl == "1" and spieler.gold >= 60:
        spieler.gold -= 60
        spieler.strength += 10
        spieler.inventar.append("Eisenschwert")
        print("Eine feine Klinge!")
    elif wahl == "2" and spieler.gold >= 50:
        spieler.gold -= 50
        spieler.defense += 5
        spieler.inventar.append("Lederrüstung")
        print("Das wird dich schützen.")
    elif wahl == "3":
        return
    else:
        print("Nicht genug Gold oder ungültige Wahl.")
