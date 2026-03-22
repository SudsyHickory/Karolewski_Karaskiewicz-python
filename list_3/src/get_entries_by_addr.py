import sys
from common_tools import read_log, print_entries, IDX_ID_RESP_H, IDX_HOST

def get_entries_by_addr(log, addr):

    if not isinstance(addr, str) or addr == "":
        sys.stderr.write(f"Błąd get_entries_by_addr: adres musi być niepustym stringiem\n")
        return []
    
    if not is_valid_ip(addr):
        sys.stderr.write(f"Błąd get_entries_by_addr: '{addr}' nie jest poprawnym adresem IPv4\n")

    result = []

    for entry in log:

        if entry[IDX_ID_RESP_H] == addr or entry[IDX_HOST] == addr:
            result.append(entry)

    return result

def is_valid_ip(addr):

    octets = addr.split(".")

    if len(octets) != 4:
        return False
    
    for octet in octets:

        #sprawdzamy czy każdy znak w stringu jest cyfrą
        if not octet.isdigit():
            return False
        
        if int(octet) < 0 or int(octet) > 255:
            return False
        
    return True

def main():

    try:
        log = read_log()
        entries = get_entries_by_addr(log, "192.168.229.251")

        if entries == []:
            sys.stdout.write("Brak pasujących wpisów z podanym adresem IPv4\n")
        else:
            print_entries(entries)
            
    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()