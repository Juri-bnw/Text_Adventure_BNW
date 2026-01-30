import random
import faehigkeitenbaum
import math
import inventory_and_items


def trifft_angriff(angreifer, verteidiger):
    chance = 70 + (0.25*(angreifer.dex - verteidiger.dex))
    chance = max(30, min(chance, 95))
    return random.randint(1, 100) <= chance


def berechne_schaden(angreifer, verteidiger):
    basis = angreifer.strength + random.randint(0, angreifer.strength // 2)
    schaden_reduktion = (1- (verteidiger.defense / (verteidiger.defense + 100)))
    schaden = round(basis * schaden_reduktion)
    return max(1, schaden)


def berechne_faehigkeitsschaden(spieler, faehigkeit):
    skaliert = int(faehigkeit.base_dmg +
                   spieler.strength * getattr(faehigkeit, "scale_strength", 0) +
                   spieler.dex * getattr(faehigkeit, "scale_dex", 0) +
                   spieler.energy * getattr(faehigkeit, "scale_energy", 0) +
                   spieler.charisma * getattr(faehigkeit, "scale_charisma", 0) +
                   spieler.luck * getattr(faehigkeit, "scale_luck", 0))
    return skaliert


def waehle_zufallsgegner(gegner_liste):
    lebende = [g for g in gegner_liste if g.current_HP > 0]
    if not lebende:
        return None
    return random.choice(lebende)


def standard_angriff(spieler, gegner_liste):
    ziel = waehle_zufallsgegner(gegner_liste)
    if not ziel:
        return
    if trifft_angriff(spieler, ziel):
        schaden = berechne_schaden(spieler, ziel)
        ziel.current_HP -= schaden
        ziel.current_HP = max(0, ziel.current_HP)
        print(f"{spieler.name} trifft {ziel.name} für {schaden} Schaden!")
    else:
        print(f"{spieler.name} verfehlt!")


def nutze_faehigkeit(spieler, gegner_liste, faehigkeit):
    if spieler.current_mana < faehigkeit.mana_cost:
        print("Nicht genug Mana!")
        return False

    spieler.current_mana -= faehigkeit.mana_cost
    schaden = berechne_faehigkeitsschaden(spieler, faehigkeit)

    if faehigkeit.ziel_typ == "gegner":
        if faehigkeit.ziel_anzahl == "alle":
            print(f"{spieler.name} wirkt {faehigkeit.name} auf alle Gegner!")
            for g in gegner_liste:
                if trifft_angriff(spieler, g) == True:
                    if g.current_HP > 0:
                        schaden_reduktion = (1- ((g.defense / (g.defense + 100))))
                        g.current_HP -= round(max(1, (schaden * schaden_reduktion)))
                        g.current_HP = max(0, g.current_HP)
                        print(f"  {g.name} erleidet", round(max(1, (schaden * schaden_reduktion))) ," Schaden")
                if trifft_angriff(spieler, g) == False:
                    print(f"Angriff verfehlt {g}")
        else:
            ziel = waehle_zufallsgegner(gegner_liste)
            if not ziel:
                return False
            if trifft_angriff(spieler, ziel) == True:
                schaden_reduktion = (1- ((ziel.defense / (ziel.defense + 100))))
                ziel.current_HP -= round(max(1, (schaden * schaden_reduktion)))
                ziel.current_HP = max(0, ziel.current_HP)
                print(f"{spieler.name} wirkt {faehigkeit.name} auf {ziel.name} (", round(max(1, (schaden * schaden_reduktion))) ," Schaden)")
            if trifft_angriff(spieler, ziel) == False:
                print("Angriff verfehlt ")

    elif faehigkeit.ziel_typ == "spieler":
        spieler.current_HP += schaden
        spieler.current_HP = min(spieler.max_HP, spieler.current_HP)
        print(f"{spieler.name} heilt sich um {schaden} HP")

    return True


def gegenstaende_menue(spieler):
    if not spieler.inventar:
        print("\nInventar ist leer.")
        input("Weiter...")
        return False

    print("\nDein Inventar:")
    nutzbare = [item for item in spieler.inventar if item.typ in ["Heiltrank", "Manatrank"]]

    if not nutzbare:
        print("Keine nutzbaren Gegenstände (Tränke) im Kampf.")
        input("Weiter...")
        return False

    for i, item in enumerate(nutzbare, 1):
        print(f"{i}) {item.name} ({item.boni})")
    print(f"{len(nutzbare) + 1}) Zurück")

    wahl = input("> ")
    if wahl.isdigit():
        idx = int(wahl) - 1
        if idx == len(nutzbare):
            return False
        if 0 <= idx < len(nutzbare):
            item = nutzbare[idx]
            bonus_val = inventory_and_items.parse_bonus(item.boni)

            if item.typ == "Heiltrank":
                if "%" in item.boni:
                    spieler.current_HP = spieler.max_HP
                else:
                    spieler.current_HP = min(spieler.max_HP, spieler.current_HP + bonus_val)
                print(f"Du nutzt {item.name}!")
            elif item.typ == "Manatrank":
                if "%" in item.boni:
                    spieler.current_mana = spieler.max_mana
                else:
                    spieler.current_mana = min(spieler.max_mana, spieler.current_mana + bonus_val)
                print(f"Du nutzt {item.name}!")

            spieler.inventar.remove(item)
            return True
    return False


def gegner_phase(gegner_liste, spieler):
    for g in gegner_liste:
        if g.current_HP <= 0:
            continue
        print(f"{g.name} greift an!")
        standard_angriff(g, [spieler])
        if spieler.current_HP <= 0:
            print(f"{spieler.name} ist besiegt...")
            return


def fliehen(spieler, gegner_liste):
    ziel = waehle_zufallsgegner(gegner_liste)
    if not ziel:
        return True
    chance = 30 + (spieler.dex - ziel.dex)
    chance = max(10, min(chance, 90))
    if random.randint(1, 100) <= chance:
        print(f"{spieler.name} konnte fliehen!")
        return True
    else:
        print(f"{spieler.name} konnte nicht fliehen!")
        return False


def kampf(spieler, gegner_liste):
    spieler.current_mana = spieler.max_mana
    print("\n Kampf beginnt!")

    while spieler.current_HP > 0 and any(g.current_HP > 0 for g in gegner_liste):

        print(f"\n{spieler.name} HP: {spieler.current_HP} | Mana: {spieler.current_mana}")
        for g in gegner_liste:
            print(f"{g.name} HP: {g.current_HP}")

        turn_taken = False

        while not turn_taken:
            print("\nAktion wählen:")
            print("1) Standardangriff")
            print("2) Fähigkeiten")
            print("3) Fliehen")
            print("4) Inventar")

            wahl = input("> ")

            if wahl == "1":
                standard_angriff(spieler, gegner_liste)
                turn_taken = True

            elif wahl == "2":
                print("\nDeine Fähigkeiten:")
                for i, f in enumerate(spieler.faehigkeiten, start=1):
                    print(f"{i}) {f.name} (Mana: {f.mana_cost})")

                wahl_skill = input("> ")
                if wahl_skill.isdigit() and 1 <= int(wahl_skill) <= len(spieler.faehigkeiten):
                    skill = spieler.faehigkeiten[int(wahl_skill) - 1]
                    if nutze_faehigkeit(spieler, gegner_liste, skill):
                        turn_taken = True
                else:
                    print("Ungültige Auswahl")

            elif wahl == "3":
                if fliehen(spieler, gegner_liste):
                    return
                turn_taken = True

            elif wahl == "4":
                if gegenstaende_menue(spieler):
                    turn_taken = True

        if not any(g.current_HP > 0 for g in gegner_liste):
            print("\nAlle Gegner wurden besiegt!")
            gold_gesamt = 0
            exp_gesamt = 0
            for g in gegner_liste:
                gold_belohnung = random.randint(10, 30) + (g.level * 2)
                gold_gesamt += gold_belohnung
                exp_gesamt += g.exp_give

            spieler.gold += gold_gesamt
            spieler.exp += exp_gesamt
            print(f"Du hast {gold_gesamt} Gold und {exp_gesamt} EP erhalten!")
            print(f"Aktuelles Gold: {spieler.gold}")
            return

        if turn_taken:
            gegner_phase(gegner_liste, spieler)