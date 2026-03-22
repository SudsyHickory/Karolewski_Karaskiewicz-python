import sys
from common_tools import read_log, print_entries, IDX_STATUS_CODE

def get_failed_reads(log, merge=False):

    errors_4xx = []
    errors_5xx = []

    for entry in log:

        status_code = entry[IDX_STATUS_CODE]

        #pomijamy wpisy bez kodu statusu
        if status_code is None:
            continue

        if 400 <= status_code <= 499:
            errors_4xx.append(entry)
        elif 500 <= status_code <= 599:
            errors_5xx.append(entry)

    #jeśli merge=TRUE to zwracamy jedną listę
    if merge:
        return errors_4xx + errors_5xx
    
    #jeśli merge=FALSE to zwracamy krotkę
    return (errors_4xx, errors_5xx)

def main():

    try:
        log = read_log()

        errors_4xx, errors_5xx = get_failed_reads(log, merge=False)

        if errors_4xx == []:
            sys.stdout.write("Brak pasujących wpisów z kodem błędu 4xx\n")
        else:
            sys.stdout.write("Wpisy z kodem błędu 4xx:\n")
            print_entries(errors_4xx)

        if errors_5xx == []:
            sys.stdout.write("Brak pasujących wpisów z kodem błędu 5xx\n")
        else:
            sys.stdout.write("Wpisy z kodem błędu 5xx:\n")
            print_entries(errors_5xx)

        all_errors = get_failed_reads(log, merge=True)

        if all_errors == []:
            sys.stdout.write("Brak pasujących wpisów z kodami błędu 4xx i 5xx\n")
        else:
            sys.stdout.write("Wpisy z kodami błędu 4xx i 5xx:\n")
            print_entries(all_errors)

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()