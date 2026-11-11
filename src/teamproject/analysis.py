
def find_birthday_groups(people: list[dict]) -> dict[tuple[int, int], list[int]]:
    """Findet Personen mit gleichem Geburtstag.

    Args:
        people: Liste von Dictionaries mit id, name und birthdate.

    Returns:
        Dictionary mit (Monat, Tag) als Schlüssel und sortierten
        Personen-IDs als Wert. Nur Gruppen mit mindestens zwei Personen.
    """

    # Erstellt ein leeres Dictionary für die Geburtstagsgruppen.
    groups = {}

    # Geht alle Personen durch.
    for person in people:

        # Speichert das Geburtsdatum.
        birthdate = person["birthdate"]

        # Verwendet nur Monat und Tag, nicht das Geburtsjahr.
        birthday = (birthdate.month, birthdate.day)

        # Erstellt eine neue Gruppe, wenn der Geburtstag noch nicht existiert.
        if birthday not in groups:
            groups[birthday] = []

        # Fügt die Personen-ID zur passenden Gruppe hinzu.
        groups[birthday].append(person["id"])

    # Erstellt das Dictionary für das endgültige Ergebnis.
    birthday_groups = {}

    # Geht alle Geburtstagsgruppen durch.
    for birthday, ids in groups.items():

        # Ignoriert Gruppen mit nur einer Person.
        if len(ids) >= 2:

            # Sortiert die IDs aufsteigend.
            ids.sort()

            # Speichert die gültige Gruppe.
            birthday_groups[birthday] = ids

    # Gibt die Geburtstagsgruppen zurück.
    return birthday_groups
