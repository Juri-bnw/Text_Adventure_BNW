import random
import gegner

MAP_OPTIONEN = [
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
    moegliche_gegner = GEGNER_PRO_ORT[ort]

    anzahl_gegner = random.randint(1, 3)  # 1 bis 3 Gegner
    gegner_liste = random.choices(moegliche_gegner, k=anzahl_gegner)

    print("Gegner tauchen auf:")
    for g in gegner_liste:
        print(f" - {g.name}")

    return "kampf", gegner_liste



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
        return None

    return aktion