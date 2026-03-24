import sys
from common_tools import read_log, print_entries, IDX_URI

def get_entries_by_extension(log, ext):
    
    if not isinstance(ext, str) or ext == "":
        sys.stderr.write("Błąd get_entries_by_extension: rozszerzenie musi być niepustym stringiem\n")
        return []
    
    #zamiana podanego rozszerzenia na małe litery i usunięcie kropek z lewej strony (np. .JPG na jpg)
    ext_lower = ext.lower().lstrip(".")

    result = []

    for entry in log:

        uri = entry[IDX_URI]

        if get_uri_extension(uri) == ext_lower:
            result.append(entry)

    return result

#wyciągnięcie rozszerzenia (np. "jpg") z URI
def get_uri_extension(uri):

    if uri is None or uri == "-" or uri == "":
        return ""
    
    question_position = uri.find("?")

    #odcinamy parametry po znaku "?"
    if question_position != -1:
        uri = uri[:question_position]

    #szukamy ostatniej kropki w URI
    dot_position = uri.rfind(".")

    if dot_position == -1:
        return ""
    
    #sprawdzamy czy po kropce są jakieś znaki (rozszerzenie)
    extension = uri[dot_position + 1:]

    if not extension:
        return ""
    
    return extension.lower()

def main():

    try:
        log = read_log()
        entries = get_entries_by_extension(log, "jpg")

        if entries == []:
            sys.stdout.write("Brak pasujących wpisów z podanym rozszerzeniem\n")
        else:
            print_entries(entries)

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()