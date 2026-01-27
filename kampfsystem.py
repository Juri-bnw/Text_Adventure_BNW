import random
import faehigkeitenbaum

def trifft_angriff(angreifer, verteidiger):
    chance = 70 + (angreifer.dex - verteidiger.dex)
    chance = max(20, min(chance, 90))
    return random.randint(1, 100) <= chance

def berechne_schaden(angreifer, verteidiger):
    basis = angreifer.strength + random.randint(0, angreifer.strength // 2)
    schaden = basis - verteidiger.defense
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
        if faehigkeit.ziel_anzahl == 1:
            ziel = waehle_zufallsgegner(gegner_liste)
            if not ziel:
                return False
            ziel.current_HP -= schaden
            print(f"{spieler.name} wirkt {faehigkeit.name} auf {ziel.name} ({schaden} Schaden)")

        elif faehigkeit.ziel_anzahl == "alle":
            print(f"{spieler.name} wirkt {faehigkeit.name} auf alle Gegner!")
            for g in gegner_liste:
                if g.current_HP > 0:
                    g.current_HP -= schaden
                    print(f"  {g.name} erleidet {schaden} Schaden")

    elif faehigkeit.ziel_typ == "spieler":
        spieler.current_HP += schaden
        print(f"{spieler.name} heilt sich um {schaden} HP")         # FÜR HEILUNG !!!! --> hier ist schaden = heilung

    return True

######################################################## PLATZHALTER FÜR ZUKUNFT - DA KOMMEN DIE SKILL REIN ######################

def gegenstaende_menue(spieler):
    print("\nGegenstände:\nNoch keine Gegenstände vorhanden.")
    input("Weiter...")
    return False

#####################################################################################################################

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
    # Zufälliger Gegner für Fluchtchance
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



########################################################## DER KERN: DER KAMPF !!! ####################################

def kampf(spieler, gegner_liste):
    spieler.current_mana = spieler.max_mana
    print("\n Kampf beginnt!")
    while spieler.current_HP > 0 and any(g.current_HP > 0 for g in gegner_liste):
        print(f"\n{spieler.name} HP: {spieler.current_HP} | Mana: {spieler.current_mana}")
        for g in gegner_liste:
            print(f"{g.name} HP: {g.current_HP}")
        print("\nAktion wählen:")
        print("1) Standardangriff")
        print("2) Fähigkeiten")
        print("3) Fliehen")

        wahl = input("> ")

        if wahl == "1":
            standard_angriff(spieler, gegner_liste)

        elif wahl == "2":
            if not spieler.faehigkeiten:
                print("Du hast noch keine Fähigkeiten!")            # zurzeit haben nur Barbr und Zauberer skills - ob man skill-los startet und später welche lernt - mal gucken
                continue

            print("\nDeine Fähigkeiten:")
            for i, f in enumerate(spieler.faehigkeiten, start=1):
                print(f"{i}) {f.name} (Mana: {f.mana_cost})")
            wahl_skill = input("> ")

            if wahl_skill.isdigit() and 1 <= int(wahl_skill) <= len(spieler.faehigkeiten):
                skill = spieler.faehigkeiten[int(wahl_skill) - 1]
                nutze_faehigkeit(spieler, gegner_liste, skill)

            else:
                print("Ungültige Auswahl")
                continue

        elif wahl == "3":
            if fliehen(spieler, gegner_liste):
                return
            continue

                aktuelle_gegner = [g for g in aktuelle_gegner if g.current_HP > 0]
        if not aktuelle_gegner:
            print("Alle Gegner wurden besiegt!")
            gold_gewinn = random.randint(10, 30)
            spieler.gold += gold_gewinn
            print(f"Du hast {gold_gewinn} Gold gefunden! (Gesamt: {spieler.gold})")
            return
        gegner_phase(aktuelle_gegner, spieler)

        gegner_liste = [g for g in gegner_liste if g.current_HP > 0]

        if not gegner_liste:
            print("Alle Gegner wurden besiegt!")
            return

        gegner_phase(gegner_liste, spieler)
