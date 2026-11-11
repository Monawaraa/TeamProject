# Anforderungen
## Eingabedatei einlesen
### Anforderungen
#### Allgemein
- CSV ist utf-8 codiert
- CSV enthält die exakt Spalten "id,name,datum"
- Seperator ist Komma
#### Wichtige Anforderungen
- id ist eine postive Zahl
- id ist einmalig
- Namen müssen nach Entfernen äußerer Leerzeichen nicht leer sein
- Namen müssen nicht eindeutig sein
- äußere Leerzeichen in Feldern werden ignoriert
- ungültige Pflichtdaten führen zu ValueError
- die exakte Formulierung der Fehlermeldung ist nicht vorgegeben
### Testing
- ValueError bei falschen, fehlenden oder zu vielen Spalten
## Datumsformate
### Anforderungen
- Unterstützte Formate: *YYYY-MM-DD* und *DD.MM.YYYY*
- Im deutschen Format dürfen Tag und Monat ein- oder zweistellig sein
- Das Datum muss tatsächlich existieren
- ValueError bspw. bei "29.02.2001" und "31.02.2001"
- ValueError bei nicht unterstütztes Format
- frühestes Datum ist 01.01.1900
- ValueError bei früheren als frühestes Datum
### Testing

## Altersähnlichkeit
### Anforderungen
#### Altersähnlichkeit
- Zwei Personen sind sich umso ähnlicher im Alter, je kleiner der absolute Abstand ihrer Geburtsdaten in
Tagen ist
#### Altersnachbarn
- eine Person ist niemals ihr eigener Nachbar,
- standardmäßig werden maximal 10 Nachbarn geliefert,
- gibt es weniger andere Personen, werden alle verfügbaren Personen geliefert,
- zuerst wird nach kleinstem Datumsabstand sortiert,
- bei gleichem Abstand gewinnt die kleinere ID,
- das Ergebnis darf nicht von der Reihenfolge der CSV-Zeilen abhängen,
- für dieses Praktikum gilt n >= 0 ; bei n == 0 erhält jede Person eine leere Nachbarliste
### Testing

## Gleicher Geburstag
### Anforderungen
- "Gleicher Geburtstag" bedeutet: gleicher Monat und gleicher Tag, unabhängig vom Geburtsjahr
- Gruppen mit nur einer Person werden nicht zurückgegeben
- innerhalb einer Gruppe werden IDs aufsteigend sortiert
- jede Person darf nur einmal in einer Gruppe vorkommen

## Verhalten Leerer Datensatz
### Anforderungen
- Eine CSV-Datei mit korrektem Header, aber ohne Personen ist erlaubt
### Testing
- load_people(...) == []
- find_age_neighbors([]) == {}
- find_birthday_groups([]) == {}

## Funktionen
### Anforderungen
- parse_date ist in dates.py
- parse_date bekommt str
- parse_date returned date
- load_people ist in people.py
- load_people bekommt sr
- load_people returned eine liste mit dict
- find_age_neighbors ist in analysis.py
- find_age_neighbors bekommt (list mit dict, integer)
- find_age_neighbors returned dict{int: list[int]}
- find_birthday_groups ist in analysis.py
- find_birthday_groups bekommt list mit dict
- find_birthday_groups returned dict{tuple[int,int]:list[int]}
- tuple[int,int] ist der Geburtstag
### Testing


