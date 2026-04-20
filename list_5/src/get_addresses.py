import re
from parse_csv import parse_stations_metadata

def get_addresses(path, city):

    #wzorzec dla adresu z ulicą i opcjonalnym numerem np. "ul. Grota Roweckiego 6"
    address_pattern = re.compile(
        r"^"
        r"(?:ul\.|al\.)?" #sprawdzamy czy w adresie jest ul. lub al. na początku, "?:" - nie tworzy grupy, "(...)?" - może wystąpić ale nie musi
        r"\s*" #zero lub więcej białych znaków
        r"(.+?)" #stworzenie 1 grupy: "." - dowolny znak, "+" - przynajmniej jeden znak, "?" - przejście do następnej grupy gdy pojawią się znaki pasujące do kolejnej grupy
        r"\s*"
        r"(\d+\w*)?" #"\d+" – jedna lub więcej cyfr, "\w*" - zero lub więcej cyfr lub liter
        r"\s*"
        r"$"
    )

    result = []

    stations = parse_stations_metadata(path)

    for station in stations:

        if station.miejscowosc.lower() != city.lower() or not station.wojewodztwo or not station.adres:
            continue

        match = address_pattern.match(station.adres)

        if match:
            ulica = match.group(1)
            numer = match.group(2)

            result.append((station.wojewodztwo, station.miejscowosc, ulica, numer if numer else ""))

    return result

def main():

    adresy = get_addresses("stacje.csv", "Wrocław")
    
    if adresy:
            for wojewodztwo, miasto, ulica, numer in adresy:
                print(f"Województwo: {wojewodztwo}, Miasto: {miasto}, Ulica: {ulica}, Numer: {numer if numer else 'brak'}")
    else:
        print("Brak stacji w podanej miejscowości")

if __name__ == "__main__":
    main()