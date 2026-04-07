import os
import sys
import subprocess
import json
from collections import Counter

def run_manager(directory_path):
    # Lista do przechowywania wyników z każdego pliku
    results_list = []
    
    # Sprawdzenie czy katalog istnieje
    if not os.path.isdir(directory_path):
        print(f"Blad: {directory_path} nie jest katalogiem.")
        return

    # Przechodzenie przez pliki w katalogu
    for filename in os.listdir(directory_path):
         
        # Tylko pliki tekstowe
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            
            if os.path.isfile(file_path):
                try:
                    result = subprocess.run(
                    [sys.executable, 'analyze_file.py'],
                    input=file_path,
                    capture_output=True,
                    text=True
                    )

                    if result.returncode == 0:
                        file_data = json.loads(result.stdout)
                        results_list.append(file_data) # Zapisujemy do listy słowników
                    else:
                        print(f"Blad: {result.stderr}")
                        
                except Exception as e:
                    print(f"Wyjatek przy pliku {filename}: {e}")

    print_stats(results_list)

def print_stats(results_list):

    #Statystyki
    total_files = len(results_list)
    
    if total_files == 0:
        print("\n--- RAPORT ZBIORCZY ---")
        print("Nie znaleziono danych do przetworzenia.")
        return

    total_chars = sum(d.get('total_characters', 0) for d in results_list)
    total_words = sum(d.get('total_words', 0) for d in results_list)
    total_lines = sum(d.get('total_lines', 0) for d in results_list)
    
    global_chars = Counter()
    global_words = Counter()
    
    for d in results_list:
        if 'chars_freq' in d:
            global_chars.update(d['chars_freq'])  #dodajemy ze soba dane ze slownikow
        if 'words_freq' in d:
            global_words.update(d['words_freq'])

    print("\n--- RAPORT ZBIORCZY ---")
    print(f"Liczba przeczytanych plikow: {total_files}")
    print(f"Sumaryczna liczba znakow:    {total_chars}")
    print(f"Sumaryczna liczba slow:      {total_words}")
    print(f"Sumaryczna liczba wierszy:   {total_lines}")
    
    if global_chars:
        char, count = global_chars.most_common(1)[0]
        print(f"Znak wystepujacy najczesciej: '{char}' (wystapil {count} razy)")
    if global_words:
        word, count = global_words.most_common(1)[0]
        print(f"Slowo wystepujace najczesciej: '{word}' (wystapilo {count} razy)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Podaj: python manager.py <sciezka_do_katalogu>")
    else:
        run_manager(sys.argv[1])