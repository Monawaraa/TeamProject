from datetime import date as dt


def parse_time(text:str):
    if not text:
        raise ValueError("Datum darf nicht leer sein.")

    if len(text) not in [8, 9, 10]:
        raise ValueError("Datum muss im richtigen Format sein.")

    if "." in text:
        date = dt.strptime(text, "%d.%m.%y")

    if "-" in text:
        date = dt.strptime(text, "%y-%m-%d")


    return date