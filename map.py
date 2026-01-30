import random
import gegner
import copy

MAP_OPTIONEN = [
    "wiese",
    "dunkler_wald",
    "verlassene_huette",
    "rasten",
    "marktplatz",
    "ruine",
    "unterwelt",
    "schloss",
    "tempel",
    "wüste",
    "gasthof",
    "ruinen",
]

GEGNER_PRO_ORT = {
    "ruine": [gegner.Skelett, gegner.Fledermaus],
    "wiese": [gegner.Skelett, gegner.Ratte, gegner.Fledermaus, gegner.Schleim],
    "dunkler_wald": [gegner.Dunkler_Magier, gegner.Fledermaus, gegner.Schleim, gegner.Spinne, gegner.Zombie,
                     gegner.Wolf],
    "verlassene_huette": [gegner.Skelett, gegner.Dunkler_Magier, gegner.Spinne, gegner.Zombie, ],
    "wüste": [gegner.Skelett, gegner.Zombie, gegner.Spinne, gegner.Schlange, ],
    "ruinen": [gegner.Geist, gegner.Bandit, gegner.Dunkler_Magier, gegner.Goblin, gegner.Spinne],
    "unterwelt": [gegner.Ork, gegner.Drache, gegner.Daemon],
    "schloss": [gegner.Soldat, gegner.Geist, gegner.Bandit],
    "tempel": [gegner.Wolf, gegner.Schlange, gegner.Schleim]
}


def erkunden(ort):
    if ort == "marktplatz":
        return "marktplatz", None

    moegliche_gegner = GEGNER_PRO_ORT[ort]

    anzahl_gegner = random.randint(1, 3)  # 1 bis 3 Gegner
    gegner_liste = [copy.deepcopy(random.choice(moegliche_gegner)) for _ in range(anzahl_gegner)]

    print("Gegner tauchen auf:")
    for g in gegner_liste:
        print(f" - {g.name}")

    return "kampf", gegner_liste


def fuehre_aktion_aus(aktion, spieler):
    if aktion == "wiese" or aktion == "dunkler_wald" or aktion == "verlassene_huette" or aktion == "ruinen" or aktion == "ruine" or aktion == "wüste" or aktion == "unterwelt" or aktion == "schloss" or aktion == "tempel":
        return erkunden(aktion)
    elif aktion == "marktplatz":
        return "marktplatz", None
    elif aktion == "gasthof":
        gasthof(spieler)
        return None
    elif aktion == "rasten":
        rasten(spieler)
        return None
    elif aktion == "inventar":
        return "inventar", None


def rasten(spieler):
    hp_heilung = int(spieler.max_HP * 0.1)

    spieler.current_HP += hp_heilung
    if spieler.current_HP > spieler.max_HP:
        spieler.current_HP = spieler.max_HP
        print(f"Du bist vollständig geheilt und hast im Moment {spieler.current_HP} / {spieler.max_HP} HP")
    else:
        print(f"Du rastest und erhältst {hp_heilung} HP. Im Moment hast du {spieler.current_HP} / {spieler.max_HP} HP.")


def gasthof(spieler):
    hp_heilung = int(spieler.max_HP * 0.25)

    spieler.current_HP += hp_heilung
    if spieler.current_HP > spieler.max_HP:
        spieler.current_HP = spieler.max_HP
        print(f"Du bist vollständig geheilt und hast im Moment {spieler.current_HP} / {spieler.max_HP} HP")
    else:
        print(f"Du rastest und erhältst {hp_heilung} HP. Im Moment hast du {spieler.current_HP} / {spieler.max_HP} HP.")



aktionen_zaehler = 0
tag = 1


def map_loop(spieler):
    global aktionen_zaehler, tag

    optionen = random.sample(MAP_OPTIONEN, 3)
    print(f"\nTag {tag}")
    print("Was möchtest du tun?")

    for i, opt in enumerate(optionen, start=1):
        print(f"{i}) {opt.replace('_', ' ').title()}")

    wahl = input("> ")
    if wahl not in ["1", "2", "3"]:
        print("Ungültige Eingabe.")
        return map_loop(spieler)

    aktion = optionen[int(wahl) - 1]
    aktionen_zaehler += 1

    if aktionen_zaehler >= 5:
        tag += 1
        print("------------------------------------------------------------")
        print("                EIN NEUER TAG BEGINNT")
        print("------------------------------------------------------------")
        aktionen_zaehler = 0
        print("\nEin Tag vergeht...\n")
        return None

    return aktion
