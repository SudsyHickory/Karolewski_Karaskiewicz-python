import os
import sys

#funkcja zwracająca listę katalogów z PATH
def get_path_directories():

    path = os.environ.get("PATH", "") #pobranie wartości zmiennej PATH w formie stringa
    directories_list = directories_list = [d for d in path.split(os.pathsep) if d] #podzielenie stringa na listę katalogów względem seperatora systemowego (na WINDOWS ";", na LINUX ":") - zapisujemy tylko niepuste stringi

    return directories_list

#funkcja zwracająca wszystkie pliki wykonywalne w podanym katalogu
def get_executable_files(directory):

    if not os.path.isdir(directory):
        return None #zwrócenie None gdy katalog nie istnieje
    
    try:
        dir_elements = os.listdir(directory) #pobranie listy plików i katalogów z podanego katalogu
    
    except PermissionError:
        return None #zwrócenie None gdy nie ma dostępu do katalogu
    
    result = []

    for dir_element in dir_elements:

        full_path = os.path.join(directory, dir_element) #połącznie katalogu z elementem (np "C:\\Windows" + "plik.exe" -> "C:\\Windows\\plik.exe")

        if os.path.isfile(full_path) and is_executable(full_path): #sprawdzenie czy element jest plikiem i czy jest wykonywalny
            result.append(dir_element)

    return sorted(result)

def is_executable(file_path):

    if sys.platform == "win32": #sprawdzenie czy program działa na systemie Windows
        _, extension = os.path.splitext(file_path) #ignorujemy nazwę i pobieramy rozszerzenie pliku
        return extension.lower() in (".exe", ".bat", ".cmd") #zwracamy True jeśli rozszerzenie jest rozszerzeniem dla plików wykonywalnych
    
    return os.access(file_path, os.X_OK) #dla systemów Unix sprawdzamy czy plik ma ustawiony bit wykonywalności

def print_directories_with_files(directories):

    for directory in directories:

        print(f"\n{directory}")

        files = get_executable_files(directory)

        if files is None:
            print(f"Brak dostępu do katalogu '{directory}' lub katalog nie istnieje")

        elif files:
            for file in files:
                print(f" {file}")

        else:
            print(f"W katalogu '{directory}' nie ma plików wykonywalnych")

def main():

    if len(sys.argv) < 2:
        print("\nKomendy:")
        print(f"python {sys.argv[0]} --list         #wyświetl katalogi z PATH")
        print(f"python {sys.argv[0]} --executables  #wyświetl katalogi z plikami wykonywalnymi z PATH")
        sys.exit(1)

    parametr = sys.argv[1]
    directories = get_path_directories()

    if parametr == "--list":
        for directory in directories:
            print(directory)

    elif parametr == "--executables":
        print_directories_with_files(directories)

    else:
        print(f"Nieznany parametr: {parametr}")
        sys.exit(1)

if __name__ == "__main__":
    main()