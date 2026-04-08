import os
import sys
import json
from collections import Counter

#funkcja zwaracająca liczbę znaków w pliku
def count_characters(content):
    return len([c for c in content if not c.isspace()])

#funkcja zwracająca liczbę słów w pliku
def count_words(content):
    return len(content.split())

#funkcja zwracająca liczbę wierszy w pliku
def count_lines(lines):
    return len(lines)

#funkcja zwracająca najczęściej występujący znak w pliku
def get_most_common_character(content):

    filtered = [c for c in content if not c.isspace()]

    if not filtered:
        return None
    
    counter = Counter(filtered)
    most_common = counter.most_common(1)[0][0]

    return most_common, dict(counter)

#funkcja zwracająca najczęściej występujące słowo w pliku
def get_most_common_word(content):
    
    words = content.lower().split()

    if not words:
        return None
    
    counter = Counter(words)
    most_common = counter.most_common(1)[0][0]

    return most_common, dict(counter)

#funkcja analizująca plik i zwracająca wynik jako słownik
def analyze_file(file_path):

    file = open(file_path, "r", encoding="utf-8")

    lines = file.readlines()
    content = "".join(lines)

    file.close()

    most_common_char, chars_dict = get_most_common_character(content)
    most_common_word, words_dict = get_most_common_word(content)

    result = {
        "file_path": file_path,
        "total_characters": count_characters(content),
        "total_words": count_words(content),
        "total_lines": count_lines(lines),
        "most_common_character": most_common_char,
        "chars_freq": chars_dict,
        "most_common_word": most_common_word,
        "words_freq": words_dict
    }

    return result

def main():

    file_path = sys.stdin.readline().strip() #czytamy sciezke

    if not file_path: 
        return

    if not os.path.isfile(file_path):
        sys.stderr.write(f"Błąd: plik '{file_path}' nie istnieje")
        sys.exit(1)

    result = analyze_file(file_path)

    sys.stdout.write("\n" + json.dumps(result, ensure_ascii=False) + "\n") #json.dumps(result) - zamienia słownik na tekst w formacie JSON; ensure_ascii=False - pozwala na polskie znaki

if __name__ == "__main__":
    main()