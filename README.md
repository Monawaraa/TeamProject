# TeamProject 
~ 05 TeamProject ~

# 

# Birthday Projekt Geburtstage & Altersnachbarn

Woran arbeiten wir? An einer Python-Library zur Verarbeitung und Analyse von Personendaten aus CSV-Dateien. Unser Projekt berechnet Altersnachbarn anhand des absoluten Datumsabstands und gruppiert Personen nach demselben Geburtstag!! :)


## Team & Rollenverteilung

* **Product Owner / Integration:** Mona
* **Software Development:** Reza + Malte
* **Test Team:** Sabrina
* **Review / Release:** Ricarda


## Setup & Installation


1. **Repository klonen:**
   ```bash
   git clone "https://github.com/Monawaraa/TeamProject.git"
   ```

2. **Kanban-Board anlegen**
   ```
    Backlog
    Ready
    In Progress
    Review
    Done
   ```


## 1. Rollen im Team



### Product Owner / Integration (Mona)
* Offene Anforderungen sammeln
* Fragen an den Kunden (aka Prof/Tutor) formulieren
* Entscheidungen in `specification.md` dokumentieren
* Issues anlegen und priorisieren
* Issues Personen zuweisen
* Darauf achten, dass alle dieselben Schnittstellen verwenden
* Integration koordinieren
* Bei Konflikten zwischen Tests, Implementierung und Spezifikation moderieren

### Test Team (Sabrina)
* Anforderungen in Tests übersetzen
* Normalfälle, Grenzfälle und Fehlerfälle identifizieren
* Tests möglichst aus der Spezifikation entwickeln
* Nicht nur die aktuelle Implementierung „nachtesten“
* Test-PRs erstellen
* Nach Änderungen Regressionen prüfen

*(Hinweis: Das Test Team klärt mit dem Software Team Rückfragen zu Schnittstellen, soll seine Erwartungen aber nicht einfach aus dessen Code ableiten.)*

### Software Development (Malte & Reza)
* Implementierung der vereinbarten Funktionen
* Kleine verständliche Module
* Einhaltung der vereinbarten API
* Lokale Tests während der Entwicklung
* Kleine Commits
* Pull Requests pro Issue oder zusammenhängender Änderung

*(Hinweis: Schnittstellen werden nicht eigenmächtig verändert.)*

### Review / Release (Ricarda)
* Pull Requests auf Verständlichkeit und Umfang prüfen
* CI-Ergebnisse beobachten
* Prüfen, ob ein PR wirklich zum Issue passt
* Auf unbeabsichtigte API-Änderungen achten
* Merge-Konflikte begleiten
* Vor dem Abschluss die Definition of Done kontrollieren


##
##
## Phase 1 – Teamstart und Board

### Zielstruktur der Module
```text
src/TeamProject/
├── __init__.py
├── csv_reader.py   # rohe CSV-Zeilen lesen 
├── dates.py        # Datumsstrings interpretieren
├── people.py       # Personen validieren und laden
└── analysis.py     # Altersnachbarn und Geburtstagsgruppen
```

### Product Owner / Integration
* GitHub Repository erstellen und Teammitglieder dazu einladen
* Team-Fork kontrollieren
* Kanban-Board anlegen (Spalten: `Backlog`, `Ready`, `In Progress`, `Review`, `Done`)
* Rollen im README oder in einem Issue dokumentieren
* Erstes Issue „Spezifikation prüfen und dokumentieren“ erstellen

### Test Team
* GitHub Repository lokal klonen
* `uv sync` ausführen
* Vorhandene Tests prüfen
* Erste Fragen sammeln: Was müsste man wissen, bevor man Tests schreiben kann?

### Software Development
* GitHub Repository lokal klonen
* Projektstruktur und vorhandenen CSV-Reader ansehen
* Noch keine fachliche Implementierung beginnen
* Technische Fragen zur vorgesehenen API sammeln

### Review / Release
* GitHub Repository lokal klonen
* Prüfen, ob alle denselben Team-Fork verwenden
* Prüfen, ob CI auf dem Fork läuft
* Überprüfen, dass niemand direkt auf `main` arbeitet

## Ergebnis der Phase
* Gemeinsames Repository funktioniert
* Kanban-Board existiert
* Rollen sind klar
* Alle können lokal arbeiten


##

## Team-Workflow & Regeln

* **erlaubte Bibliotheken:**
csv, datetime, collections, os, pytest, ruff

* **Kein Direkt-Push:** Niemand arbeitet direkt auf `main` !!!
* **Issues & Branches:** Jede Aufgabe wird als Issue im Kanban-Board angelegt, einer Person zugewiesen (`assigned`) und in einem eigenen Branch bearbeitet (z. B. `feature/12-date-parsing` oder `test/15-input-validation`).
* **WIP-Limit:** Maximal **drei Issues** dürfen sich gleichzeitig in der Spalte `In Progress` befinden.
* **Pull Requests:** PRs verlinken das zugehörige Issue (z. B. `Closes #12`) und werden vor dem Merge von mindestens einer anderen Person reviewed.
* **Spezifikation:** Alle fachlichen Details und getroffenen Teamentscheidungen sind in der `SPECIFICATION.md` dokumentiert.
