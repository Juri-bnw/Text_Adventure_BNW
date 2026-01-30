import inventory_and_items


def zeige_marktplatz(spieler):
    while True:
        print(f"\n--- MARKTPLATZ (Gold: {spieler.gold}) ---")
        print("1) Gasthaus (Essen & Heilung)")
        print("2) Alchemist (Tränke)")
        print("3) Trainer (Erfahrung & Training)")
        print("4) Schmied (Waffen & Ausrüstung)")
        print("5) Verlassen")

        wahl = input("> ")

        if wahl == "1":
            gasthaus(spieler)
        elif wahl == "2":
            shop_menue(spieler, "ALCHEMIST", inventory_and_items.ALCHEMIST_ITEMS)
        elif wahl == "3":
            trainer(spieler)
        elif wahl == "4":
            shop_menue(spieler, "SCHMIED", inventory_and_items.SCHMIED_ITEMS)
        elif wahl == "5":
            break
        else:
            print("Ungültige Auswahl.")


def shop_menue(spieler, name, items):
    while True:
        print(f"\n--- {name} (Gold: {spieler.gold}) ---")
        for i, item in enumerate(items, 1):
            print(f"{i}) {item.name} ({item.preis} Gold) - {item.boni}")
        print(f"{len(items) + 1}) Zurück")

        wahl = input("> ")
        if wahl.isdigit():
            idx = int(wahl) - 1
            if idx == len(items):
                break
            if 0 <= idx < len(items):
                item = items[idx]
                if spieler.gold >= item.preis:
                    spieler.gold -= item.preis
                    spieler.inventar.append(item)
                    bonus_val = inventory_and_items.parse_bonus(item.boni)

                    if item.typ == "Waffe":
                        if "stärke" in item.boni.lower():
                            spieler.strength += bonus_val
                        elif "geschicklichkeit" in item.boni.lower():
                            spieler.dex += bonus_val
                        elif "mana" in item.boni.lower():
                            spieler.max_mana += bonus_val
                    elif item.typ == "Ausrüstung":
                        if "hp" in item.boni.lower():
                            spieler.max_HP += bonus_val
                            spieler.current_HP += bonus_val
                        elif "verteidigung" in item.boni.lower():
                            spieler.defense += bonus_val
                        elif "geschicklichkeit" in item.boni.lower():
                            spieler.dex += bonus_val
                    print(f"Du hast {item.name} gekauft!")
                else:
                    print("Nicht genug Gold!")
        else:
            print("Ungültige Eingabe.")


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
