import re
from parse_csv import parse_stations_metadata

#4a – wyodrębnienie wszystkich dat w formacie RRRR-MM-DD
def extract_dates(stations):

    date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}") #4 cyfry, myślnik, 2 cyfry, myślnik, 2 cyfry
    dates = []

    for station in stations:

        for value in [station.data_uruchomienia, station.data_zamkniecia]:
            if value and date_pattern.match(value):
                dates.append(value)

    return dates

#4b – wyciągnięcie listy szerokości i długości geograficznych
def extract_coordinates(stations):

    coord_pattern = re.compile(r"\d+\.\d{6}") #jedna lub więcej cyfr, kropka, dokładnie 6 cyfr
    coordinates = []

    for station in stations:

        for value in [station.szerokosc_geograficzna, station.dlugosc_geograficzna]:
            if value and coord_pattern.match(value):
                coordinates.append(value)

    return coordinates

#4c – znalezienie stacji o nazwach składających się z dwóch części (zawierających myślnik)
def find_two_part_names(stations):

    two_part_pattern = re.compile(r"^[^-]+-[^-]+$") #pierwsza część - bez myślnika, myślnik, druga część - bez myślnika
    two_part_names = []

    for station in stations:

        if station.nazwa_stacji and two_part_pattern.match(station.nazwa_stacji):
            two_part_names.append(station.nazwa_stacji)

    return two_part_names

#4d – zamiana spacji na podłogę i polskich znaków diakrytycznych na odpowiedniki łacińskie
def normalize_station_names(stations):

    polish_chars = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n','ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N','Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }

    #wzorzec dla szukania polskich znaków diakrytycznych i łączenia ich w np. ą|ć|ę|ż
    polish_pattern = re.compile("|".join(c for c in polish_chars.keys()))

    normalized_names = []

    for station in stations:
        
        #zamiana każdej spacji na symbol podłogi
        name_with_underscores = re.sub(r" ", "_", station.nazwa_stacji)
        
        #lambda dla każdego znalezionego znaku zwraca jego odpowiadającą wartość ze słownika
        normalized_name = polish_pattern.sub(lambda polish_char: polish_chars[polish_char.group()], name_with_underscores)

        normalized_names.append((station.nazwa_stacji, normalized_name))

    return normalized_names

#4e – weryfikacja, czy stacje z kodem kończącym się na "MOB" mają rodzaj stacji "mobilna"
def verify_mob_stations(stations):

    mob_pattern = re.compile(r"MOB$") #"MOB" na końcu
    results = []

    for station in stations:
        
        if station.kod_stacji and mob_pattern.search(station.kod_stacji): #search szuka wzorca w dowolnym miejscu stringa (tutaj sprawdzamy koniec)
            is_mobile = station.rodzaj_stacji.lower() == "mobilna"
            results.append((station.kod_stacji, station.rodzaj_stacji, is_mobile))

    return results

#4f – znalezienie stacji o nazwach składających się z trzech części (oddzielonych myślnikiem)
def find_three_part_names(stations):

    three_part_pattern = re.compile(r"^[^-]+-[^-]+-[^-]+$")
    three_part_names = []

    for station in stations:
        
        if three_part_pattern and three_part_pattern.match(station.nazwa_stacji):
            three_part_names.append(station.nazwa_stacji)

    return three_part_names

#4g – znalezienie adresów zawierających przecinek i nazwę ulicy (ul.) lub alei (al.)
def find_addresses_with_comma_and_street(stations):

    comma_street_pattern = re.compile(r"(?=.*,)(?=.*\b(?:ul\.|al\.))") #"?=" - szuka od początku czy w stringu jest przecinek i ul. lub al., "\b" - sprawdza czy wskaźnik jest na początku słowa
    matching_addresses = []

    for stacja in stations:
        
        if stacja.adres and comma_street_pattern.search(stacja.adres):
            matching_addresses.append(stacja.adres)

    return matching_addresses

def main():
    stations = parse_stations_metadata("stacje.csv")

    print(f"4a: Daty w formacie RRRR-MM-DD: {extract_dates(stations)[:3]}")
    print(f"4b: Współrzędne geograficzne: {extract_coordinates(stations)[:3]}")
    print(f"4c: Stacje o dwuczłonowych nazwach: {find_two_part_names(stations)[:3]}")
    print(f"4d: Normalizacja nazw stacji: {normalize_station_names(stations)[:3]}")

    verified_mob_stations = verify_mob_stations(stations)
    incorrect_mob_stations = []

    for station in verified_mob_stations:

        _, _, is_mobile = station

        if not is_mobile:
            incorrect_mob_stations.append(station)

    print(f"4e: Weryfikacja stacji MOB: {incorrect_mob_stations[:3]}")
    print(f"4f: Stacje o trzyczłonowych nazwach: {find_three_part_names(stations)[:3]}")
    print(f"4g: Adresy z przecinkiem i ul./al.: {find_addresses_with_comma_and_street(stations)[:3]}")

if __name__ == "__main__":
    main()