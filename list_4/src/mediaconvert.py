import sys
import subprocess
import json
import os
import datetime
from utils import get_files_from_dir, generate_new_path


def log_history(original, converted, target_format, tool_used):
    #zapis do json
    history_file = "history.json"
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "source": original,
        "result": converted,
        "format": target_format,
        "tool": tool_used
    }
    
    history = []
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            history = json.load(f) # wczytanie tego co jest w pliku history.json, jesli istnieje
            
    history.append(entry) # dodanie nowego wpisu
    
    with open(history_file, "w") as f: # "w" to otwarcie pliku do zapisu ktore czysci historie, dlatego wczesniej ja wczytujemy
        json.dump(history,f, indent=4, ensure_ascii=False) #indent dodaje wciecia


def convert_file(input_path, target_format):
    output_path = generate_new_path(input_path, target_format)
    
    # wybor narzedzia, splitext zwraca root i ext (example_file, .txt), my pobieramy ext 
    ext = os.path.splitext(input_path)[1].lower()
    
    if ext in ['.mp4', '.avi', '.mp3', '.wav', '.webm']:
        tool = "ffmpeg"
        cmd = ["ffmpeg", "-i", input_path, output_path] # stworzenie cmd musi byc -i, skrot od input 
    elif ext in ['.jpg', '.png', '.bmp', '.gif']:
        tool = "imagemagick"
        magick_exec = os.environ.get('MAGICK_PATH', 'magick') #pobranie zmiennej srodowiskowej dla magick, albo zostawienie magick
        cmd = [magick_exec, input_path, output_path] # stworzenie cmd, nie musi byc -i
    else:
        print(f"Pominięto nieobsługiwany format: {input_path}")
        return

    try:
        print(f"Konwertowanie {input_path} -> {target_format}...")
        subprocess.run(cmd, check=True, capture_output=True) #uruchomienie nowego procesu z wrzuconym cmd
        log_history(input_path, output_path, target_format, tool) #zapisanie do history.json
        print("Sukces!")
    except subprocess.CalledProcessError as e:
        print(f"Błąd konwersji {input_path}: {e}")
    

def main():
    if len(sys.argv) < 3:
        print("Podaj: python mediaconvert.py <katalog> <format>")
        return
    
    input_dir = sys.argv[1]
    target_format = sys.argv[2]

    files = get_files_from_dir(input_dir)
    for file in files:
        convert_file(file, target_format)

if __name__ == "__main__":
    main()