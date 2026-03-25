import sys
from common_tools import *

def detect_sus(log, threshold):
    sus_log = {}

    for entry in log:
        ip = entry[IDX_ID_ORIG_H]
        status = entry[IDX_STATUS_CODE]

        if ip not in sus_log:
            sus_log[ip] = {"total": 0, "errors": 0}

        sus_log[ip]["total"] += 1
        if status == 404:
            sus_log[ip]["errors"] += 1

    suspects = []
    
    for ip,counts in sus_log.items():
        if counts["total"]>threshold or counts["errors"] > (threshold / 2): 
            suspects.append(ip)

    return suspects

def main():

    try:
        log = read_log()
        suspects = detect_sus(log, 2000)
        print("Podejrzane adresy IP:")
        for ip in suspects:
            print(f" - {ip}")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()