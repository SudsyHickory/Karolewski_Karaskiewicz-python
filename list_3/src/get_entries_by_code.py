import sys
from common_tools import read_log, print_entries, IDX_STATUS_CODE

def get_entries_by_code(log, code):
    
    if not isinstance(code, int):
        sys.stderr.write("Błąd: get_entries_by_code: kod statusu musi być liczbą całkowitą\n")
        return []
    
    if code < 100 or code > 599:
        sys.stderr.write(f"Blad get_entries_by_code: kod statusu {code} jest poza zakresem HTTP (100-599)\n")
        return []
    
    result = []

    for entry in log:
        
        if entry[IDX_STATUS_CODE] == code:
            result.append(entry)

    return result

def main():

    try:
        log = read_log()
        entries = get_entries_by_code(log, 200)

        if entries == []:
            sys.stdout.write("Brak pasujących wpisów z podanym kodem HTTP\n")
        else:
            print_entries(entries)

    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()