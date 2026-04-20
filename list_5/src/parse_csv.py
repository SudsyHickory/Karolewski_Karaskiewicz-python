import csv
from collections import namedtuple

#struktura dla metadanych stacji pomiarowej
StationMetadata = namedtuple("StationMetadata", [ #krotka, której możemy nadać nazwy pól
    "nr",
    "kod_stacji",
    "kod_miedzynarodowy",
    "nazwa_stacji",
    "stary_kod_stacji",
    "data_uruchomienia",
    "data_zamkniecia",
    "typ_stacji",
    "typ_obszaru",
    "rodzaj_stacji",
    "wojewodztwo",
    "miejscowosc",
    "adres",
    "dlugosc_geograficzna",
    "szerokosc_geograficzna"
])

#struktura dla pojedynczego pomiaru
Measurement = namedtuple("Measurement", [
    "nr",
    "kod_stacji",
    "wskaznik",
    "czas_usredniania",
    "jednostka",
    "kod_stanowiska",
    "data",
    "wartosc"
])

#funkcja parsująca plik z metadanymi stacji (stacje.csv)
def parse_stations_metadata(path):

    stations = []

    with open(path, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file) #każdy wiersz z pliku CSV zapisujemy jako słownik, którego kluczami są nazwy kolumn z pierwszego wiersza pliku CSV

        for row in reader:
            
            station = StationMetadata(
                nr=row.get("Nr", "").strip(),
                kod_stacji=row.get("Kod stacji", "").strip(), #do pola kod_stacji pobieramy wartość ze słownika o kluczu "Kod stacji"
                kod_miedzynarodowy=row.get("Kod międzynarodowy", "").strip(),
                nazwa_stacji=row.get("Nazwa stacji", "").strip(),
                stary_kod_stacji=row.get("Stary Kod stacji \n(o ile inny od aktualnego)", "").strip(),
                data_uruchomienia=row.get("Data uruchomienia", "").strip(),
                data_zamkniecia=row.get("Data zamknięcia", "").strip(),
                typ_stacji=row.get("Typ stacji", "").strip(),
                typ_obszaru=row.get("Typ obszaru", "").strip(),
                rodzaj_stacji=row.get("Rodzaj stacji", "").strip(),
                wojewodztwo=row.get("Województwo", "").strip(),
                miejscowosc=row.get("Miejscowość", "").strip(),
                adres=row.get("Adres", "").strip(),
                dlugosc_geograficzna=row.get("WGS84 φ N", "").strip(),
                szerokosc_geograficzna=row.get("WGS84 λ E", "").strip()
            )

            stations.append(station)

    return stations

#funkcja parsująca plik z pomiarami (measurements/*.csv)
def parse_measurements(path):

    measurements = []

    with open(path, "r", encoding="utf-8") as file:

        reader = list(csv.reader(file)) #zapisujemy dane w postacii listy

        nr = reader[0][1:]
        station_codes = reader[1][1:]
        indicators = reader[2][1:]
        averaging_time = reader[3][1:]
        units = reader[4][1:]
        monitoring_point_codes = reader[5][1:]

        for row in reader[6:]:

            if not row:
                continue

            date = row[0]
            
            for i, value in enumerate(row[1:]):

                if i >= len(station_codes):
                    break

                try:
                    value = float(value) if value else None
                except ValueError:
                    value = None
                
                measurements.append(Measurement(
                    nr = nr[i].strip(),
                    kod_stacji = station_codes[i].strip(),
                    wskaznik = indicators[i].strip(),
                    czas_usredniania = averaging_time[i].strip(),
                    jednostka = units[i].strip(),
                    kod_stanowiska = monitoring_point_codes[i].strip(),
                    data = date.strip(),
                    wartosc = value
                ))

    return measurements

def main():

    print("\nParsowanie pliku z metadanymi stacji (stacje.csv):")

    stations = parse_stations_metadata("stacje.csv")
    print(f"Liczba wczytanych stacji: {len(stations)}")

    if stations:
        print("\nPierwsze 3 stacje:")
        for station in stations[:3]:
            print(f"{station}\n")
    else:
        print("Nie znaleziono żadnych stacji")



    print("\nParsowanie pliku z pomiarami (measurements/2023_As(PM10)_24g.csv):")

    measurements = parse_measurements("measurements/2023_As(PM10)_24g.csv")
    print(f"Liczba wczytanych pomiarów: {len(measurements)}")
    
    if measurements:
        print("\nPierwsze 3 pomiary:")
        for measurement in measurements[:3]:
            print(f"{measurement}\n")
    else:
        print("Nie znaleziono żadnych pomiarów")

if __name__ == "__main__":
    main()