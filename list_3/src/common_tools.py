import sys
import datetime

SEPARATOR ="\t"

IDX_TS = 0
IDX_UID = 1
IDX_ID_ORIG_H = 2
IDX_ID_ORIG_P = 3
IDX_ID_RESP_H = 4
IDX_ID_RESP_P = 5
IDX_METHOD = 6
IDX_HOST = 7
IDX_URI = 8
IDX_STATUS_CODE = 9

#konwersja danych dla znaczników czasowych
def parse_timestamp(value):

    if value == "-" or value == "": #"-" jest znacznikiem brakujących danych w pliku
        return None #None informuje że pole danych nie istnieje
    
    try:
        ts_float = float(value) #najpierw musimy zamienić value na float bo pobierając to pole ze stdin, value jest stringiem
        return datetime.datetime.fromtimestamp(ts_float) #ta funkcja oczekuje float
    except (ValueError, OSError, OverflowError): #string nie jest liczbą; system nie obsługuje tej daty; za duża liczba
        return None

#konwersja danych dla portów, kodów statusu itp.
def parse_field(value, type):

    if value == "-" or value == "":
        return None
    
    try:
        return type(value) #zwracamy zkonwertowaną daną
    except (ValueError, TypeError):
        return None
    
def parse_line(line):

    line = line.strip()

    #ignorujemy puste linie
    if not line:
        return None
    
    #dzielimy linię na pola
    fields = line.split(SEPARATOR)

    #chcemy aby linia miała co najmniej 15 pól
    if len(fields) < 15:
        sys.stderr.write(f"Linia ma mniej niż 15 pól, liczba pól linii: {len(fields)}\n")
        return None
    
    #konwertujemy dane w każdym polu
    ts = parse_timestamp(fields[0])
    uid = fields[1]
    id_orig_h = fields[2]
    id_orig_p = parse_field(fields[3], int)
    id_resp_h = fields[4]
    id_resp_p = parse_field(fields[5], int)
    method = fields[7]
    host = fields[8]
    uri = fields[9]
    status_code = parse_field(fields[14], int)

    #zwracamy krotkę
    return (ts, uid, id_orig_h, id_orig_p, id_resp_h, id_resp_p, method, host, uri, status_code)

def read_log():
    
    entries = []

    for line in sys.stdin:

        entry = parse_line(line)

        if entry is not None:
            entries.append(entry)

    return entries

def print_entries(entries):

    for entry in entries:
        sys.stdout.write(str(entry) + "\n") #konwersja krotki na stringa