import os
import sys

#funkcja zwracająca słownik zmiennych pasujących do filtrów
def get_filtred_variables(variables, filters):

    result = {}

    for name, value in variables.items():

        for filter in filters:
            
            if filter.lower() in name.lower():
                result[name] = value
                break #wychodzimy z pętli filtrów - nie sprawdzamy kolejnych filtrów gdy już znajdziemy dopasowanie

    return result

#funkcja zwracająca zmienne posortowane względem nazw kluczy w kolejności alfabetycznej
def get_sorted_variables(variables):

    result = []
    
    for name in sorted(variables.keys()):
        result.append(f"{name}={variables[name]}\n")

    return result

def main():

    #domyślnie do zmiennej variables zapisujemy wszystkie zmienne środowiskowe
    variables = os.environ

    #wśród argumentów linii komend, filtrami są wszystkie następne argumenty od pozycji 1 (bo na pozycji 0 jest nazwa uruchomianego pliku, czyli print_env_vars)
    filters = sys.argv[1:]

    if filters:
        variables = get_filtred_variables(variables, filters)

    if not variables:
        sys.stderr.write(f"Brak zmiennych środowiskowcyh pasujących do podanych filtrów: {filters}\n")
        return
    
    lines = get_sorted_variables(variables)

    for line in lines:
        sys.stdout.write(line + "\n")

if __name__ == "__main__":
    main()