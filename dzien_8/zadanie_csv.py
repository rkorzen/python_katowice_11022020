"""
Pobierz z sieci jakiś plik csv

https://dane.gov.pl/dataset/1489,dane-teleadresowe-jst-w-polsce

Wybierz z csv jakieś kolumny i zapisz to w osobnym pliku csv

"""
import csv
with open("dane_in.csv") as f:
    reader = csv.DictReader(f, delimiter=";")
    dane = []
    for row in reader:
        dane.append((row['Kod_TERYT'], row['telefon kierunkowy'] + row['telefon'].replace(" ", "" ).replace("\n", "")))

with open("dane_out.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["TERYT", "TELEFON"])
    writer.writerows(dane)