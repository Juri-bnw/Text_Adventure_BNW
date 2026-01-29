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

Eisenschwert = Gegenstand("Eisenschwert", "Waffe", "+10 Stärke")

Eisenbogen = Gegenstand("Eisenbogen", "Waffe", "+10 Geschicklichkeit")

Eisenstab = Gegenstand("Eisenstab", "Waffe", "+10 Mana")

Eisendolch = Gegenstand("Eisendolch", "Waffe", "+10 Geschicklichkeit")

Eisenhelm = Gegenstand("Eisenhelm", "Ausrüstung", "+10 HP")

Eisenruestung = Gegenstand("Eisenrüstung", "Ausrüstung", "+10 Verteidigung")

Eisenarmschienen = Gegenstand("Eisenarmschienen", "Ausrüstung", "+10 Geschicklichkeit")

Eisenhandschuhe = Gegenstand("Eisenhandschuhe", "Ausrüstung", "+10 Verteidigung")

Eisenhose = Gegenstand("Eisenhose", "Ausrüstung", "+10 Geshicklichkeit")

Eisenschuhe = Gegenstand("Eisenschuhe", "Ausrüstung", "+10 Geschicklichkeit")

Silberschwert = Gegenstand("Silberschwert", "Waffe", "+50 Stärke")

Silberbogen = Gegenstand("Silberbogen", "Waffe", "+50 Geschicklichkeit")

Silberstab = Gegenstand("Silberstab", "Waffe", "+50 Mana")

Silberdolch = Gegenstand("Silberdolch", "Waffe", "+50 Geschicklichkeit")

Silberhelm = Gegenstand("Silberhelm", "Ausrüstung", "+50 HP")

Silberruestung = Gegenstand("Silberrüstung", "Ausrüstung", "+50 Verteidigung")

Silberarmschienen = Gegenstand("Silberarmschienen", "Ausrüstung", "+50 Geschicklichkeit")

Silberhandschuhe = Gegenstand("Silberhandschuhe", "Ausrüstung", "+50 Verteidigung")

Silberhose = Gegenstand("Silberhose", "Ausrüstung", "+50 Geschicklichkeit")

Silberschuhe = Gegenstand("Silberschuhe", "Ausrüstung", "+50 Geschicklichkeit")
