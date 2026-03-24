import sys
from common_tools import read_log, print_entries

def main():

    try:
        log = read_log()
        print_entries(log)

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()