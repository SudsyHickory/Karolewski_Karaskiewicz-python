import sys
from log_to_dict import *

def get_most_active_session(log_dict):
    if not log_dict:
        return None
    
    # Znajduje klucz (UID), dla którego wartość (lista wpisów) ma największą długość.
    # lambda określa kryterium porównania: zamiast nazw kluczy, porównujemy liczebność ich list.
    most_active_uid = max(log_dict, key=lambda uid: len(log_dict[uid]))
    return most_active_uid, len(log_dict[most_active_uid])


def main():

    try:
        log = read_log()
        log_dict = log_to_dict(log)
        uid,count = get_most_active_session(log_dict)
        if uid:
            print(f"Najaktywniejsza sesja: {uid} (liczba zapytań: {count})")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()