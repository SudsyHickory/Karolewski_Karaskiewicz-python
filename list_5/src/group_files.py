import re
from pathlib import Path

def group_measurement_files_by_key(path):

    #wzorzec dla nazwy pliku: <rok>_<mierzona wielkość>_<częstotliwość>.csv np. "2023_As(PM10)_24g.csv"
    pattern = re.compile(
        r"^" #początek stringa
        r"(\d{4})" #stworzenie 1 grupy: "\d{4}"" - dokładnie 4 cyfry na początku nazwy
        r"_" #podkreślnik
        r"([^_]+)" #stworzenie 2 grupy: "[^_]+" - jeden lub więcej znaków niebędących podkreślnikiem
        r"_"
        r"([^_]+)" #stworzenie 3 grupy 
        r"\.csv" #.csv na końcu nazwy
        r"$"
    )

    result = {}

    for file_path in path.iterdir():

        if not file_path.is_file(): #pomijamy podkatalogi
            continue

        match = pattern.match(file_path.name) #próbujemy dopasować nazwę pliku do wzorca

        if match:
            rok = match.group(1)
            wielkosc = match.group(2)
            czestotliwosc = match.group(3)

            klucz = (rok, wielkosc, czestotliwosc)
            result[klucz] = file_path

    return result

def main():

    path = Path("measurements")

    grupy = group_measurement_files_by_key(path)

    if grupy:

        for (rok, wielkosc, czestotliwosc), sciezka in grupy.items():
            print(f"Klucz: rok={rok}, wielkość={wielkosc}, częstotliwość={czestotliwosc}")
            print(f"Plik: {sciezka}\n")
    else:
        print("Brak plików pasujących do podanego wzorca")

if __name__ == "__main__":
    main()