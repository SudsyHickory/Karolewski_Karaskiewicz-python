import sys
from common_tools import read_log, IDX_METHOD

def count_by_method(log):

    method_counts = {}

    for entry in log:

        method = entry[IDX_METHOD]

        if method is None or method == "-" or method == "":
            continue

        if method in method_counts:
            method_counts[method] += 1
        else:
            method_counts[method] = 1

    return method_counts
    
def main():

    try:
        log = read_log()
        methods = count_by_method(log)
 
        sys.stdout.write(str(methods) + "\n")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()