import os
import sys
import time

#funkcja parsująca argumenty linii komend
def parse_arguments(arguments):

    lines_count = 10
    follow_mode = False
    file_path = None

    for argument in arguments:

        if argument.startswith("--lines="):

            value = argument.split("=", 1)[1] #podzielenie argumentu jeden raz po pierwszym znaku "=" i zapisanie drugiego elementu

            if not value.isdigit():
                return None, None, None #zwracamy None gdy wartość agumentu --lines nie jest liczbą

            lines_count = int(value)

        elif argument == "--follow":
            follow_mode = True

        else:
            if file_path is None:
                file_path = argument
            else:
                return None, None, None #zwracamy None gdy podano za dużo argumentów - czyli więcej niż jeden plik

    return lines_count, follow_mode, file_path

#funkcja zwracająca podaną liczbę ostatnich linii z podanej ścieżki pliku
def read_from_file(file_path, lines_count):

    file = open(file_path, "r", encoding="utf-8") #otworzenie pliku tylko do odczytu i z uwzględnieniem polskich znaków
    all_lines = file.readlines()
    last_lines = all_lines[-lines_count:] #pobranie linii od końca

    return last_lines, file

#funkcja zwracająca podaną liczbę ostatnich linii z wejścia standardowego
def read_from_stdin(lines_count):

    all_lines = sys.stdin.readlines()
    last_lines = all_lines[-lines_count:]

    return last_lines

#funkcja śledząca zawartość pliku i czekająca na nowe linie
def follow_file(file, file_path):

    file.seek(0, 2) #ustawienie wskaźnika odczytu pliku na koniec pliku

    while True:
        current_position = file.tell() #funkcja tell() zwraca aktualną pozycję wskaźnika odczytu pliku
        line = file.readline()

        if not line:
            time.sleep(0.1)

            current_size = os.stat(file_path).st_size #pobieramy aktualny rozmiar pliku w bajtach (pole st_size obiektu os.stat(file_path))

            #sprawdzamy czy plik nie został skrócony
            if current_position > current_size:
                file.seek(0) #ustawienie wskaźnika odczytu pliku na początek pliku

        else:
            sys.stdout.write(line + "\n")

def main():

    lines_count, follow_mode, file_path = parse_arguments(sys.argv[1:])

    if lines_count is None:
        sys.stderr.write(f"Błąd: podano nieprawidłowe dane wejściowe")
        sys.exit(1)

    #jeśli podano ścieżkę pliku to ignorujemy wejście standardowe
    if file_path is not None:

        if not os.path.isfile(file_path):
            sys.stderr.write(f"Błąd: plik '{file_path}' nie istnieje")
            sys.exit(1)

        last_lines, file = read_from_file(file_path, lines_count)
        
        for line in last_lines:
            sys.stdout.write(line + "\n")

        if follow_mode:
            try:
                follow_file(file, file_path)
            except KeyboardInterrupt:
                pass #przy naciśnięciu CTRL+C program w konsoli zostanie przerwany a wyjątek zostanie zignorowany
            finally:
                file.close()
        else:
            file.close()

    #obsługa programu dla wejścia standardowego
    else:
        if follow_mode:
            sys.stderr.write("\nUwaga: --follow działa tylko z plikiem, nie ze stdin\n\n") #bo przy wejściu standardowym program dostaje dane pliku przez potok tylko jeden raz

        last_lines = read_from_stdin(lines_count)
        
        for line in last_lines:
            sys.stdout.write(line + "\n")

if __name__ == "__main__":
    main()