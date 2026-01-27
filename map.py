import random
import gegner

MAP_OPTIONEN = [
    "erkunden",
    "wiese",
    "dunkler_wald",
    "verlassene_huette",
    "rasten"
]

GEGNER_PRO_ORT = {
    "wiese": [gegner.Skelett, gegner.Ratte, gegner.Fledermaus],
    "dunkler_wald": [gegner.Dunkler_Magier, gegner.Fledermaus],
    "verlassene_huette": [gegner.Skelett, gegner.Dunkler_Magier]
}

def erkunden(ort):
    gegner_liste = GEGNER_PRO_ORT[ort]
    gegner_auswahl = random.choice(gegner_liste)  # jetzt Objekt, kein String
    print(f"Ein Gegner taucht auf: {gegner_auswahl.name}!")
    return "kampf", gegner_auswahl


def fuehre_aktion_aus(aktion, spieler):
    if aktion == "wiese" or aktion == "dunkler_wald" or aktion == "verlassene_huette":
        return erkunden(aktion)
    elif aktion == "rasten":
        rasten(spieler)
        return None
    elif aktion == "nichts":
        print("Du gehst ein Stück weiter. Nichts passiert.")
        return None


def rasten(spieler):
    hp_heilung = int(spieler.max_HP * 0.1)

    spieler.current_HP += hp_heilung
    if spieler.current_HP > spieler.max_HP:
        spieler.current_HP = spieler.max_HP
        hp_heilung = 0
        print(f"Du bist vollständig geheilt und hast im Moment {spieler.current_HP} / {spieler.max_HP} HP")
    else: print(f"Du rastest und erhältst {hp_heilung} HP. Im Moment hast du {spieler.current_HP} / {spieler.max_HP} HP.")

def Erkunde_Wiese(gegner_liste):
    gegner_im_ort_liste = [gegner.Fledermaus]
    gegner = random.choice(gegner_liste)
    print("Ein Gegner taucht auf!")
    return "kampf", gegner


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

    aktion = optionen[int(wahl)-1]
    aktionen_zaehler += 1

    if aktionen_zaehler >= 5:
        tag += 1
        aktionen_zaehler = 0
        print("\nEin Tag vergeht...\n")

    return aktion