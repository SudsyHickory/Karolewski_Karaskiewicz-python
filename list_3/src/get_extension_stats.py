import sys
from common_tools import *

def get_extension_stats(log):
    extensions_counts = {}

    for entry in log:
        uri = entry[IDX_URI]
        if not uri or uri == "-":
            continue
        
        # Odcinamy wszystko co po '?'
        path = uri.split('?')[0]

        if '.' in path:

            # Wszystko po kropce bierzemy
            extension = path.split('.')[-1].lower()
            if extension in extensions_counts:
                extensions_counts[extension] +=1
            else:
                extensions_counts[extension] = 1
    
    return extensions_counts

def main():

    try:
        log = read_log()
        stats = get_extension_stats(log)
        for key, value in stats.items():
            sys.stdout.write(f"{key} {value}\n")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()