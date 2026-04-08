import os
import datetime



def get_output_dir():
    output_dir = os.environ.get('CONVERTED_DIR', 'converted') #zwraca conveted_dir gdy istnieje zmienna srodowiskowa, inaczej converted

    #gdy brak zmiennej srodowiskowej, tworzymy katalog converted
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir


def generate_new_path(original_path, target_ext):
    output_dir = get_output_dir()
    base_name = os.path.splitext(os.path.basename(original_path))[0] #splitext zwraca root i ext (example_file, .txt), my pobieramy root 
    date_str = datetime.datetime.now().strftime("%Y%m%d")

    new_filename = f"{date_str}-{base_name}.{target_ext}"

    return os.path.join(output_dir, new_filename) #laczymy nazwe pliku z docelowym katalogiem

def get_files_from_dir(directory):

    #pobranie plikow z danego directory
    results_list = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory,filename)
        if os.path.isfile(file_path):
            results_list.append(file_path)
    return results_list

