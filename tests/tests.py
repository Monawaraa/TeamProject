import pytest

'''CSV READER testen'''
from csv_reader import read_csv_rows

path1 = r"tests\testdata\form_csv.csv"
def test_fromread_csv():
    assert read_csv_rows == [{
                    "id": "1001",
                    "name": "Anna Keller",
                    "datum": "2001-09-14",
                }{
                    "id": "1002",
                    "name": "Ben Koch",
                    "datum": "17.03.2000",
                }]

path1 = r"tests\testdata\non_form1.csv"
path2 = 

def test_fromread_csv():
    with pytest.raises(ValueError):
