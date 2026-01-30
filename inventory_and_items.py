class Gegenstand:
    def __init__(self, name, typ, boni, preis=0):
        self.name = name
        self.typ = typ
        self.boni = boni
        self.preis = preis

# Helper to parse bonus value (e.g., "+10 HP" -> 10)
def parse_bonus(bonus_str):
    try:
        return int(bonus_str.split()[0].replace("+", "").replace("%", ""))
    except:
        return 0

# Items definieren
kleiner_Heiltrank = Gegenstand("kleiner Heiltrank", "Heiltrank", "+10 HP", 20)
mittlerer_Heiltrank = Gegenstand("mittlerer Heiltrank", "Heiltrank", "+100 HP", 100)
grosser_Heiltrank = Gegenstand("großer Heiltrank", "Heiltrank", "+500 HP", 400)
ultimativer_Heiltrank = Gegenstand("ultimativer Heiltrank", "Heiltrank", "+100% HP", 2000)

kleiner_Manatrank = Gegenstand("kleiner Manatrank", "Manatrank", "+10 Mana", 20)
mittlerer_Manatrank = Gegenstand("mittlerer Manatrank", "Manatrank", "+100 Mana", 100)
grosser_Manatrank = Gegenstand("großer Manatrank", "Manatrank", "+500 Mana", 400)
ultimativer_Manatrank = Gegenstand("ultimativer Manatrank", "Manatrank", "+100% Mana", 2000)

Bronzeschwert = Gegenstand("Bronzeschwert", "Waffe", "+10 Stärke", 60)
Bronzebogen = Gegenstand("Bronzebogen", "Waffe", "+10 Geschicklichkeit", 60)
Bronzestab = Gegenstand("Bronzestab", "Waffe", "+10 Mana", 60)
Bronzedolch = Gegenstand("Bronzedolch", "Waffe", "+10 Geschicklichkeit", 60)

Bronzehelm = Gegenstand("Bronzehelm", "Ausrüstung", "+10 HP", 50)
Bronzeruestung = Gegenstand("Bronzerüstung", "Ausrüstung", "+10 Verteidigung", 100)
Bronzearmschienen = Gegenstand("Bronzearmschienen", "Ausrüstung", "+10 Geschicklichkeit", 40)
Bronzehandschuhe = Gegenstand("Bronzehandschuhe", "Ausrüstung", "+10 Verteidigung", 40)
Bronzehose = Gegenstand("Bronzehose", "Ausrüstung", "+10 Geschicklichkeit", 60)
Bronzeschuhe = Gegenstand("Bronzeschuhe", "Ausrüstung", "+10 Geschicklichkeit", 40)

Eisenschwert = Gegenstand("Eisenschwert", "Waffe", "+50 Stärke", 300)
Eisenbogen = Gegenstand("Eisenbogen", "Waffe", "+50 Geschicklichkeit", 300)
Eisenstab = Gegenstand("Eisenstab", "Waffe", "+50 Mana", 300)
Eisendolch = Gegenstand("Eisendolch", "Waffe", "+50 Geschicklichkeit", 300)

Eisenhelm = Gegenstand("Eisenhelm", "Ausrüstung", "+50 HP", 250)
Eisenruestung = Gegenstand("Eisenrüstung", "Ausrüstung", "+50 Verteidigung", 500)
Eisenarmschienen = Gegenstand("Eisenarmschienen", "Ausrüstung", "+50 Geschicklichkeit", 200)
Eisenhandschuhe = Gegenstand("Eisenhandschuhe", "Ausrüstung", "+50 Verteidigung", 200)
Eisenhose = Gegenstand("Eisenhose", "Ausrüstung", "+50 Geshicklichkeit", 300)
Eisenschuhe = Gegenstand("Eisenschuhe", "Ausrüstung", "+50 Geschicklichkeit", 200)

Silberschwert = Gegenstand("Silberschwert", "Waffe", "+100 Stärke", 600)
Silberbogen = Gegenstand("Silberbogen", "Waffe", "+100 Geschicklichkeit", 600)
Silberstab = Gegenstand("Silberstab", "Waffe", "+100 Mana", 600)
Silberdolch = Gegenstand("Silberdolch", "Waffe", "+100 Geschicklichkeit", 600)

Silberhelm = Gegenstand("Silberhelm", "Ausrüstung", "+100 HP", 500)
Silberruestung = Gegenstand("Silberrüstung", "Ausrüstung", "+100 Verteidigung", 1000)
Silberarmschienen = Gegenstand("Silberarmschienen", "Ausrüstung", "+100 Geschicklichkeit", 400)
Silberhandschuhe = Gegenstand("Silberhandschuhe", "Ausrüstung", "+100 Verteidigung", 400)
Silberhose = Gegenstand("Silberhose", "Ausrüstung", "+100 Geschicklichkeit", 600)
Silberschuhe = Gegenstand("Silberschuhe", "Ausrüstung", "+100 Geschicklichkeit", 400)

Goldschwert = Gegenstand("Goldschwert", "Waffe", "+500 Stärke", 3000)
Goldbogen = Gegenstand("Goldbogen", "Waffe", "+500 Geschicklichkeit", 3000)
Goldstab = Gegenstand("Goldstab", "Waffe", "+500 Mana", 3000)
Golddolch = Gegenstand("Golddolch", "Waffe", "+500 Geschicklichkeit", 3000)

Goldhelm = Gegenstand("Goldhelm", "Ausrüstung", "+500 HP", 2500)
Goldruestung = Gegenstand("Goldrüstung", "Ausrüstung", "+500 Verteidigung", 5000)
Goldarmschienen = Gegenstand("Goldarmschienen", "Ausrüstung", "+500 Geschicklichkeit", 2000)
Goldhandschuhe = Gegenstand("Goldhandschuhe", "Ausrüstung", "+500 Verteidigung", 2000)
Goldhose = Gegenstand("Goldhose", "Ausrüstung", "+500 Geschicklichkeit", 3000)
Goldschuhe = Gegenstand("Goldschuhe", "Ausrüstung", "+500 Geschicklichkeit", 2000)

ALCHEMIST_ITEMS = [kleiner_Heiltrank, mittlerer_Heiltrank, grosser_Heiltrank, ultimativer_Heiltrank,
                   kleiner_Manatrank, mittlerer_Manatrank, grosser_Manatrank, ultimativer_Manatrank]

SCHMIED_ITEMS = [Bronzeschwert, Bronzebogen, Bronzestab, Bronzedolch,
                 Bronzehelm, Bronzeruestung, Bronzearmschienen, Bronzehandschuhe, Bronzehose, Bronzeschuhe,
                 Eisenschwert, Eisenbogen, Eisenstab, Eisendolch,
                 Eisenhelm, Eisenruestung, Eisenarmschienen, Eisenhandschuhe, Eisenhose, Eisenschuhe,
                 Silberschwert, Silberbogen, Silberstab, Silberdolch,
                 Silberhelm, Silberruestung, Silberarmschienen, Silberhandschuhe, Silberhose, Silberschuhe,
                 Goldschwert, Goldbogen, Goldstab, Golddolch,
                 Goldhelm, Goldruestung, Goldarmschienen, Goldhandschuhe, Goldhose, Goldschuhe]
