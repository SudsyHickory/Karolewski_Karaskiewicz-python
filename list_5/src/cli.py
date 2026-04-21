import argparse
from pathlib import Path
from group_files import group_measurement_files_by_key
import csv
import random
from datetime import datetime
from parse_csv import parse_stations_metadata
import statistics
import logging
import sys


#6
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG) 

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stdout_handler.setFormatter(formatter)
    stderr_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)   #stworzenie stdout_handler i stderr aby wypisywac na rozne wyjscia w zaleznosci od logu
    logger.addHandler(stderr_handler)


def validate_date(d_str):
    try:
        dt = datetime.strptime(d_str, "%Y-%m-%d")
        logging.debug(f"Poprawnie sparsowano datę: {d_str}")
        return dt
    except ValueError:
        logging.error(f"Niepoprawny format daty: '{d_str}'. Oczekiwano RRRR-MM-DD.")
        exit(1)

#5b i
def get_random_station(file_path):
    logging.info(f"Otwieranie pliku pomiarowego: {file_path.name}")
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = list(csv.reader(f))
            station_codes = reader[1][1:]
            random_station_code = random.choice(station_codes[1:])      # z wszystkich station_code wylosowanie jednego
            
            logging.info(f"Zamknięto plik pomiarowy: {file_path.name}")
            print(f"Wylosowana stacja: {random_station_code}")

            logging.info(f"Otwieranie pliku metadanych: {"stacje.csv"}")
            all_stations = parse_stations_metadata("stacje.csv")    # pobranie wszystkich stacji, aby znalezc adres dla naszego random_station_code
            logging.info(f"Zamknięto plik metadanych: {"stacje.csv"}")

            # Szukamy tej jednej konkretnej stacji w liscie obiektow
            founded = next((s for s in all_stations if s.kod_stacji == random_station_code), None)
            
            if founded:
                print(f"Nazwa: {founded.nazwa_stacji}")
                print(f"Województwo: {founded.wojewodztwo}")
                print(f"Miejscowość: {founded.miejscowosc}")
                print(f"Adres: {founded.adres}")
            else:
                logging.warning("Nie znaleziono metadanych dla tej stacji.")
    except FileNotFoundError:
        logging.error(f"Nie udało się otworzyć pliku: {file_path}")
        return

#5b ii
def get_station_stats(file_path,args,dt_start,dt_end):
    pomiary = []
    logging.info(f"Otwieranie pliku pomiarowego: {file_path.name}")
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            
            row1 = next(reader) # Wiersz z numerami
            logging.debug(f"Wiersz 1: przeczytano {len(','.join(row1).encode('utf-8'))} bajtów")
            row2 = next(reader) # Wiersz z kodami stacji
            logging.debug(f"Wiersz 2: przeczytano {len(','.join(row2).encode('utf-8'))} bajtów")
            
            try:
                # Znajdujemy numer kolumny dla podanego station_id, aby potem pracowac na pomiarach z tej kolumny
                col_index = row2.index(args.station_id)
            except ValueError:
                logging.error(f"Nie znaleziono stacji {args.station_id} w pliku.")
                return

           
            for row in reader:
                if not row: continue
                
                raw_line = ",".join(row)
                bytes_count = len(raw_line.encode('utf-8'))
                logging.debug(f"Wiersz danych: przeczytano {bytes_count} bajtów")

                try:
                    point_data = datetime.strptime(row[0], "%d/%m/%y %H:%M")   #gdy trafiamy na date, tzn ze w tym wierszu sa pomiary
                    if dt_start <= point_data <= dt_end:       # sprawdzenie czy w zakresie podanym w argumentach
                        value = row[col_index]
                        if value and value.strip():
                            pomiary.append(float(value))
                except (ValueError, IndexError):
                    continue # Pomijamy bledy parsowania daty lub puste wiersze 

        logging.info(f"Zamknięto plik pomiarowy: {file_path.name}")
    except FileNotFoundError:
        logging.error(f"Nie udało się otworzyć pliku: {file_path}")
        return
    
    #   Wyniki
    if pomiary:
        print(f"Średnia dla {args.station_id}: {statistics.mean(pomiary):.2f}")
        if len(pomiary) > 1:
            print(f"Odchylenie: {statistics.stdev(pomiary):.2f}")
    else:
        logging.warning(f"Filtr dla stacji {args.station_id} zwrócił pustą listę w datach {args.start} - {args.koniec}.")
    

def run_cli():

    parser = argparse.ArgumentParser(description="System analizy jakości powietrza GIOS")

    parser.add_argument("--wielkosc", required=True,help="Mierzona wielkość (np. PM10)")
    parser.add_argument("--czestotliwosc", required=True, help="Częstotliwość pomiaru")
    parser.add_argument("--start", required=True, help="Data początkowa (RRRR-MM-DD)")
    parser.add_argument("--koniec", required=True, help="Data końcowa (RRRR-MM-DD)")


    subparsers=parser.add_subparsers(dest="command", help="Podkomendy")

    subparsers.add_parser("random", help="Wypisz losową stację")
        
    stats_parser = subparsers.add_parser("stats", help="Oblicz statystyki dla stacji")
    stats_parser.add_argument("station_id", help="Kod stacji do analizy")


    args = parser.parse_args()

    files = group_measurement_files_by_key(Path("measurements"))    #pobranie wszystkich plikow pomiarowych
    logging.debug(f"Znaleziono {len(files)} grup plików pomiarowych.")

    #Walidacja dat
    dt_start = validate_date(args.start)
    dt_end = validate_date(args.koniec)
    year = args.start.split('-')[0]

    target_key=(year,args.wielkosc, args.czestotliwosc)     #stworzenie "klucza" z argumentow, aby znalezc konkretny plik pomiarowy

    if target_key not in files:
        logging.warning(f"Brak pliku dla klucza {target_key}. Sprawdź parametry --wielkosc i --czestotliwosc.")
        return

    file_path = files[target_key]      #pobranie konkretnego pliku pomiarowego na podstawie klucza

    if args.command == "random":
        get_random_station(file_path)
    elif args.command == "stats":
        get_station_stats(file_path,args,dt_start,dt_end)
       


if __name__ == "__main__":
    setup_logging()
    run_cli()
