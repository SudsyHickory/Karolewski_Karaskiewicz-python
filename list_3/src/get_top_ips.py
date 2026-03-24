import sys
from common_tools import read_log, IDX_ID_ORIG_H

def get_top_ips(log, n=10):

    if not isinstance(n, int) or n <= 0:
        sys.stderr.write("Błąd get_top_ips: n musi być dodatnią liczbą całkowitą\n")
        return []
    
    #słownik adresów IP
    ip_counts = {}

    for entry in log:

        ip = entry[IDX_ID_ORIG_H]

        if ip is None or ip == "-" or ip == "":
            continue

        #jeśli adres IP jest już w słowniku to zwiększamy liczbę jego wystąpień, a jeśli nie to dodajemy pierwsze wystąpienie do słownika
        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1

    #ip_counts.items() - zwraca wszystkie pary klucz-wartość ze słownika jako obiekt krotek
    #lambda pair: pair[1] - anonimowa funkcja która dla każdej krotki (ip, ip_count) zwraca drugi element – czyli liczbę wystąpień
    #sorted() - wywołuje lambda dla każdej pary i sortuje malejąco po liczbie wystąpień (reverse=True)
    ips = sorted(ip_counts.items(), key=lambda pair: pair[1], reverse=True)
    
    #zwracamy listę pierwszych n krotek
    return ips[:n]

def main():

    try:
        log = read_log()
        top_ips = get_top_ips(log, n=10)

        for ip_tuple in top_ips:
            sys.stdout.write(str(ip_tuple) + "\n")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()