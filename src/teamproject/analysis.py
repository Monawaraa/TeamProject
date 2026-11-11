def find_age_neighbors(people: list[dict], n: int = 10) -> dict[int, list[int]]:
    """Findet für jede Person die n nächsten Altersnachbarn.

    Args:
        people: Liste von Dictionaries mit id, name und birthdate.
        n: Maximale Anzahl der Nachbarn pro Person (Standard: 10).

    Returns:
        Dictionary mit Personen-IDs als Schlüssel und Listen der
        nächsten Nachbar-IDs als Werte, sortiert nach Geburtsdatumsabstand.
    """

    # Erstellt ein leeres Dictionary für die Ergebnisse.
    neighbors = {}

    # Geht jede Person in der Liste durch.
    for person in people:

        # Speichert die ID der aktuellen Person.
        person_id = person["id"]

        # Speichert das Geburtsdatum der aktuellen Person.
        birthdate = person["birthdate"]

        # Erstellt eine leere Liste für mögliche Nachbarn.
        distances = []

        # Vergleicht die aktuelle Person mit allen anderen Personen.
        for other in people:

            # Überspringt die aktuelle Person selbst.
            if other["id"] == person_id:
                continue

            # Berechnet den absoluten Abstand der Geburtsdaten in Tagen.
            distance = abs((birthdate - other["birthdate"]).days)

            # Speichert den Abstand zusammen mit der ID.
            distances.append((distance, other["id"]))

        # Sortiert zuerst nach Abstand und dann nach kleinerer ID.
        distances.sort()

        # Erstellt eine leere Liste für die IDs der nächsten Nachbarn.
        closest = []

        # Nimmt maximal n Personen aus der sortierten Liste.
        for distance, other_id in distances[:n]:

            # Fügt die ID des Nachbarn zur Ergebnisliste hinzu.
            closest.append(other_id)

        # Speichert die Nachbarn unter der ID der aktuellen Person.
        neighbors[person_id] = closest

    # Gibt alle Personen mit ihren nächsten Nachbarn zurück.
    return neighbors
