import sys
from common_tools import read_log, IDX_URI

def get_top_uris(log,n):

    if not isinstance(n, int) or n <= 0:
        sys.stderr.write("Błąd get_top_uris: n musi być dodatnią liczbą całkowitą\n")
        return []
    
    uris_counts={}

    for entry in log:
        
        uri = entry[IDX_URI]

        if uri is None or uri == "-" or uri == "":
            continue

        if uri in uris_counts:
            uris_counts[uri]+= 1
        else:
            uris_counts[uri] = 1
        
    uris = sorted(uris_counts.items(), key=lambda pair: pair[1], reverse=True)
        
    return uris[:n]
    
def main():

    try:
        log = read_log()
        top_uris = get_top_uris(log,n=10)

        for uri_tuple in top_uris:
            sys.stdout.write(str(uri_tuple) + "\n")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()