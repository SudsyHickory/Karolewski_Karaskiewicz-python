import sys
from common_tools import *

def log_to_dict(log):
    
    # Tworzymy słownik sesji, gdzie kluczem jest unikalny identyfikator UID.
    # Każdy UID wskazuje na listę słowników (zapytań) wykonanych w ramach tej samej sesji.
    sessions = {}

    for entry in log:
       
        uid = entry[IDX_UID]
        
        entry_dict = entry_to_dict(entry)
        
       
        if uid not in sessions:
            sessions[uid] = [] 
        
        sessions[uid].append(entry_dict)
        
    return sessions
        

def main():

    try:
        log = read_log()
        log_dict = log_to_dict(log)

        for uid, entries in log_dict.items():
            sys.stdout.write(str(uid)  + " " + str(entries) + "\n")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()