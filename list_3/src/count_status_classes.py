import sys
from common_tools import read_log, IDX_STATUS_CODE

def count_status_classes(log):
    
    status_counts = {"2xx": 0, "3xx": 0, "4xx": 0, "5xx": 0}

    for entry in log:
        code = entry[IDX_STATUS_CODE]
        if code is None:
            continue
        
        # Wyznaczamy pierwszą cyfrę (np. 404 // 100 = 4)
        status_class = f"{code // 100}xx"
        
        if status_class in status_counts:
            status_counts[status_class] += 1
            
    return status_counts

def main():

    try:
        log = read_log()
        status_counts = count_status_classes(log)

        for status_class, count in status_counts.items():
            sys.stdout.write(str(status_class)  + " " + str(count) + "\n")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()
