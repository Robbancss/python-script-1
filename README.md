# python-script-1
Script languages 1. assignment

Adott egy "data.txt" nevű fájl, ami egyszerű számla adatokat tartalmaz. Egy sor a számlaszámot, a számlatulajdonos nevét, az utolsó módosítás idejét és az aktuális egyenleget tartalmazza. (Az egyes elemek szóközzel vannak elválasztva.) A sorok a számlaszámok alapján rendezettek.

Minta data.txt fájl:

10001-31021 Nagy Árpád 2015.12.30. 524432
10001-31121 Zagyva László Pál 2016.03.21. 765432
10012-34321 Acél Tibor 2016.02.20. 231231
10201-11021 Lakatos Pál 2016.01.10. 2310456
10210-41011 Nagy Árpád 2016.02.03. 323532
Ezen felül adva van egy "update" nevű fájl (kiterjesztés nélkül, azaz NEM update.txt), ami a számlák adott napi változásait tartalmazza. A fájl első sora a változás dátumát adja meg, míg a többi sor a módosított számla számát, tulajdonosát, illetve a módosítás mértékét. Egy számla egy napon belül többször is módosulhat és a fájl az adott napon létrejövő számlára vonatkozó adatot (a létrehozáskor befizetett összeget) is tartalmazhat (olyan számlatulajdonos, számlaszám párost, ami eddig még nem létezett).

Minta update fájl:

2016.03.22.
10001-31021 Nagy Árpád +20000
10012-34321 Acél Tibor +35432
10012-34321 Acél Tibor -10000
10120-00123 Kiss Péter +120334
10001-31021 Nagy Árpád +5000
10210-41011 Nagy Árpád -6000
10201-11021 Lakatos Pál +100210
12345-32100 Kovács Tamás Géza +123456
A feladat egy olyan fájl elkészítése (a neve mindig legyen "newdata", szintén kiterjesztés nélkül), ami megadja a módosítás utáni aktuális számlaadatokat, az eredeti leírással megegyező formában.

Minta newdata fájl a fenti adatok esetén:

10001-31021 Nagy Árpád 2016.03.22. 549432
10001-31121 Zagyva László Pál 2016.03.21. 765432
10012-34321 Acél Tibor 2016.03.22. 256663
10120-00123 Kiss Péter 2016.03.22. 120334
10201-11021 Lakatos Pál 2016.03.22. 2410666
10210-41011 Nagy Árpád 2016.03.22. 317532
12345-32100 Kovács Tamás Géza 2016.03.22. 123456
A megoldást tartalmazó python fájl forráskódját kell feltölteni (UTF-8 kódolásnak megfelelően).