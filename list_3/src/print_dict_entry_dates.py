import sys
from log_to_dict import *
from common_tools import *

def print_dict_entry_dates(log_dict):

    for uid, entries in log_dict.items():
        
        total_req=len(entries)

        # daty
        timestamps = [e[KEY_TS] for e in entries if e[KEY_TS] is not None]
        first_req = min(timestamps) if timestamps else "N/A"
        last_req = max(timestamps) if timestamps else "N/A"

        #unikalne adresy IP / hosty
        hosts = set(e[KEY_HOST] for e in entries if e[KEY_HOST] is not None)
        orig_ips = set(e[KEY_ORIG_H] for e in entries if e[KEY_ORIG_H] is not None)

        #procentowy udzial metod http
        count_methods = {}

        for entry in entries:

            method  = entry[KEY_METHOD]

            if method is not None:
                if method in count_methods:
                    count_methods[method] += 1
                else:
                    count_methods[method] = 1
        
        #stosunek kodow 2xx do wszystkich
        counter_2xx_codes = 0
        for entry in entries:

            code = entry[KEY_STATUS]
            if code is not None and 200 <= code < 300:
                counter_2xx_codes+=1
        codes_ratio = counter_2xx_codes / total_req 

        
        print(f"Sesja: {uid}")
        print(f"Adresy IP:")
        for ip in orig_ips:
            print(f"{ip}")
        print(f"Hosty:")
        for host in hosts:
            print(f"{host}")
        print(f"Liczba żądań: {total_req}")
        print(f"Czas: {first_req} -> {last_req}")
        print("Procentowy udział metod:")
        for m, count in count_methods.items():
            percentage = (count / total_req) * 100
            print(f"    - {m}: {percentage:.2f}%")
        print(f"  Stosunek kodów 2xx: {codes_ratio:.2%}")
        print("-" * 30)


def main():

    try:
        log = read_log()
        log_dict = log_to_dict(log)
        print_dict_entry_dates(log_dict)

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()