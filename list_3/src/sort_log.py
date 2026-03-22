import sys
from common_tools import read_log, print_entries, IDX_TS

def sort_log(log, index):

    if not isinstance(index, int):
        sys.stderr.write("Błąd sort_log: indeks musi być liczbą całkowitą\n")
        return log #zwracamy oryginalną listę logów bez zmian
    
    #sprawdzamy czy lista logów jest pusta
    if not log:
        return log
    
    #sprawdzamy liczbę pól krotki
    tuple_len = len(log[0])

    #sprawdzamy czy podany index mieści się w zakresie krotki
    if index < 0 or index >= tuple_len:
        sys.stderr.write(f"Błąd sort_log: indeks {index} jest poza zakresem krotki (0-{tuple_len - 1})\n")
        return log

    def sort_key(entry):
        
        field = entry[index]
        
        if field is None: #pola z None zawsze ustawiamy na końcu
            return (1, "")
        
        return (0, field)

    try:
        return sorted(log, key=sort_key) #sorted iteruje po każdym elemencie (entry) w log i przekazuje ten element do sort_key
    except TypeError as e:
        sys.stderr.write(f"Błąd sort_log: nie można sortować po indeksie {index}: {e}\n")
        return log

def main():

    try:
        log = read_log()
        sorted_log = sort_log(log, IDX_TS)
        print_entries(sorted_log)

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()