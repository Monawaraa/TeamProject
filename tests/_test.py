import pytest

from teamproject.csv_reader import read_csv_rows

from teamproject.analysis import find_age_neighbors

'''-----------CSV READER testen------------------'''
path = r"tests\testdata\form_csv.csv"
def test_fromread_csv():
    assert read_csv_rows(path) == [{
                    "id": "1001",
                    "name": "Anna Keller",
                    "datum": "2001-09-14",
                },{
                    "id": "1002",
                    "name": "Ben Koch",
                    "datum": "17.03.2000",
                }]

path1 = r"tests\testdata\non_form1.csv"
path2 = r"tests\testdata\non_form2.csv"
path3 = r"tests\testdata\non_form3.csv"

def test_nonfromread_csv():
    with pytest.raises(ValueError):
        read_csv_rows(path1)
        read_csv_rows(path2)
        read_csv_rows(path3)

'''-----------Altersnachbarn testen------------------'''
