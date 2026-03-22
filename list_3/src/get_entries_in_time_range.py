import sys
import datetime
from common_tools import read_log, print_entries, IDX_TS

def get_entries_in_time_range(log, start, end):

    if not isinstance(start, datetime.datetime):
        sys.stderr.write("Błąd get_entries_in_time_range: 'start' musi być obiektem datetime\n")
        return []
    
    if not isinstance(end, datetime.datetime):
        sys.stderr.write("Błąd get_entries_in_time_range: 'end' musi być obiektem datetime\n")
        return []
    
    if start >= end:
        sys.stderr.write("Błąd get_entries_in_time_range: 'start' musi być wcześniej niż 'end'\n")
        return []
    
    result = []

    for entry in log:

        ts = entry[IDX_TS]

        if ts is None:
            continue

        if start <= ts < end:
            result.append(entry)

    return result

def main():

    try:
        log = read_log()
        start = datetime.datetime(2012, 3, 16, 15, 31, 36, 740000)
        end = datetime.datetime(2012, 3, 16, 15, 31, 38, 740000)
        entries = get_entries_in_time_range(log, start, end)

        if entries == []:
            sys.stdout.write("Brak pasujących wpisów w podanym przedziale czasowym\n")
        else:
            print_entries(entries)

    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")
 
 
if __name__ == "__main__":
    main()