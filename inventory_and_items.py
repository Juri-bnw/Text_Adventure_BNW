class Gegenstand:
    def __init__(self, name, typ, boni):
        self.name = name
        self.typ = typ
        self.boni = boni


kleiner_Heiltrank = Gegenstand("kleiner Heiltrank", "Heiltrank",
                               "+10 HP")  # Tränke füllen auf, Ausrüstung und Waffen erhöhen max Werte

mittlerer_Heiltrank = Gegenstand("mittlerer Heiltrank", "Heiltrank", "+100 HP")

grosser_Heiltrank = Gegenstand("großer Heiltrank", "Heiltrank", "+500 HP")

ultimativer_Heiltrank = Gegenstand("ultimativer Heiltrank", "Heiltrank", "+100% HP")

kleiner_Manattrank = Gegenstand("kleiner Manatrank", "Manatrank", "+10 Mana")

mittlerer_Manatrank = Gegenstand("mittlerer Manatrank", "Manatrank", "+100 Mana")

grosser_Manatrank = Gegenstand("großer Manatrank", "Manatrank", "+500 Mana")

ultimativer_Manatrank = Gegenstand("ultimativer Manatrank", "Manatrank", "+100% Mana")

kleiner_Erfahrungstrank = Gegenstand("kleiner Erfahrungstrank", "Erfahrungstrank", "+10 Exp")

mittlerer_Erfahrungstrank = Gegenstand("mittlerer Erfahrungstrank", "Erfahrungstrank", "+100 Exp")

grosser_Erfahrungstrank = Gegenstand("großer Erfahrungstrank", "Erfahrungstrank", "+500 Exp")

ultimativer_Erfahrungstrank = Gegenstand("ultimativer Erfahrungstrank", "Erfahrungstrank",
                                         "+100% Exp")  # +100% Exp bedeutet man bekommt 1 Level pro Trank

Bronzeschwert = Gegenstand("Bronzeschwert", "Waffe", "+10 Stärke")

Bronzebogen = Gegenstand("Bronzebogen", "Waffe", "+10 Geschicklichkeit")

Bronzestab = Gegenstand("Bronzestab", "Waffe", "+10 Mana")

Bronzedolch = Gegenstand("Bronzedolch", "Waffe", "+10 Geschicklichkeit")

Bronzehelm = Gegenstand("Bronzehelm", "Ausrüstung", "+10 HP")

Bronzeruestung = Gegenstand("Bronzerüstung", "Ausrüstung", "+10 Verteidigung")

Bronzearmschienen = Gegenstand("Bronzearmschienen", "Ausrüstung", "+10 Geschicklichkeit")

Bronzehandschuhe = Gegenstand("Bronzehandschuhe", "Ausrüstung", "+10 Verteidigung")

Bronzehose = Gegenstand("Bronzehose", "Ausrüstung", "+10 Geschicklichkeit")

Bronzeschuhe = Gegenstand("Bronzeschuhe", "Ausrüstung", "+10 Geschicklichkeit")

Eisenschwert = Gegenstand("Eisenschwert", "Waffe", "+50 Stärke")

Eisenbogen = Gegenstand("Eisenbogen", "Waffe", "+50 Geschicklichkeit")

Eisenstab = Gegenstand("Eisenstab", "Waffe", "+50 Mana")

Eisendolch = Gegenstand("Eisendolch", "Waffe", "+50 Geschicklichkeit")

Eisenhelm = Gegenstand("Eisenhelm", "Ausrüstung", "+50 HP")

Eisenruestung = Gegenstand("Eisenrüstung", "Ausrüstung", "+50 Verteidigung")

Eisenarmschienen = Gegenstand("Eisenarmschienen", "Ausrüstung", "+50 Geschicklichkeit")

Eisenhandschuhe = Gegenstand("Eisenhandschuhe", "Ausrüstung", "+50 Verteidigung")

Eisenhose = Gegenstand("Eisenhose", "Ausrüstung", "+50 Geshicklichkeit")

Eisenschuhe = Gegenstand("Eisenschuhe", "Ausrüstung", "+50 Geschicklichkeit")

Silberschwert = Gegenstand("Silberschwert", "Waffe", "+100 Stärke")

Silberbogen = Gegenstand("Silberbogen", "Waffe", "+100 Geschicklichkeit")

Silberstab = Gegenstand("Silberstab", "Waffe", "+100 Mana")

Silberdolch = Gegenstand("Silberdolch", "Waffe", "+100 Geschicklichkeit")

Silberhelm = Gegenstand("Silberhelm", "Ausrüstung", "+100 HP")

Silberruestung = Gegenstand("Silberrüstung", "Ausrüstung", "+100 Verteidigung")

Silberarmschienen = Gegenstand("Silberarmschienen", "Ausrüstung", "+100 Geschicklichkeit")

Silberhandschuhe = Gegenstand("Silberhandschuhe", "Ausrüstung", "+100 Verteidigung")

Silberhose = Gegenstand("Silberhose", "Ausrüstung", "+100 Geschicklichkeit")

Silberschuhe = Gegenstand("Silberschuhe", "Ausrüstung", "+100 Geschicklichkeit")

Goldschwert = Gegenstand("Goldschwert", "Waffe", "+500 Stärke")

Goldbogen = Gegenstand("Goldbogen", "Waffe", "+500 Geschicklichkeit")

Goldstab = Gegenstand("Goldstab", "Waffe", "+500 Mana")

Golddolch = Gegenstand("Golddolch", "Waffe", "+500 Geschicklichkeit")

Goldhelm = Gegenstand("Goldhelm", "Ausrüstung", "+500 HP")

Goldruestung = Gegenstand("Goldrüstung", "Ausrüstung", "+500 Verteidigung")

Goldarmschienen = Gegenstand("Goldarmschienen", "Ausrüstung", "+500 Geschicklichkeit")

Goldhandschuhe = Gegenstand("Goldhandschuhe", "Ausrüstung", "+500 Verteidigung")

Goldhose = Gegenstand("Goldhose", "Ausrüstung", "+500 Geschicklichkeit")

Goldschuhe = Gegenstand("Goldschuhe", "Ausrüstung", "+500 Geschicklichkeit")
