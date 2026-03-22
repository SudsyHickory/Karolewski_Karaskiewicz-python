import sys
from common_tools import read_log, IDX_METHOD

def get_unique_methods(log):

    #zbiór unikalnych metod
    unique_methods = set()

    for entry in log:

        method = entry[IDX_METHOD]

        if method is None or method == "-" or method == "":
            continue

        #set() automatycznie ignoruje duplikaty
        unique_methods.add(method)

    #konwertujemy zbiór na listę aby móc posortować
    methods = list(unique_methods)
    methods.sort()

    return methods
    
def main():

    try:
        log = read_log()
        methods = get_unique_methods(log)

        for method in methods:
            sys.stdout.write(method + "\n")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()