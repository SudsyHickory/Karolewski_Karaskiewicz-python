import logging
import time
from functools import wraps


def log(level):

    def decorator(obj):
        
        #sprawdzamy czy obj jest klasa
        if isinstance(obj, type):
            
            # Zapamietujemy oryginalny konstruktor __init__
            original_init = obj.__init__

            # Tworzymy nowe ,,opakowanie" dla konstruktora
            @wraps(original_init)
            def new_init(self, *args, **kwargs):

                logging.log(level, f"Instancjonowanie klasy: {obj.__name__}")
                original_init(self, *args, **kwargs)       # Uruchamiamy oryginalny kod konstruktora, aby przypisać pola obiektu
           
            obj.__init__ = new_init     # Podmieniamy stary __init__ na nasz nowy z logowaniem
            return obj
        else:
            # Logika dla funkcji 
            @wraps(obj)
            def wrapper(*args, **kwargs):

                start_time = time.time()
                start_str = time.ctime(start_time) #zamiana czasu na czytelna forme (np. Mon Apr 27 10:00:00 2026)
                
                result = obj(*args, **kwargs) # wywolanie funkcji
                
                duration = time.time() - start_time #ile trwala funkcja

                logging.log(level, 
                    f"Funkcja: {obj.__name__}, Start: {start_str}, "
                    f"Czas trwania: {duration:.4f}s, Arg: {args} {kwargs}, "
                    f"Wynik: {result}")
                
                return result   #zwracamy wynik do programu
            
            return wrapper      # funkcja wrapper ktora zastapi oryginal
        
    return decorator



logging.basicConfig(level=logging.DEBUG)

# Test funkcji
@log(logging.INFO)
def dodaj(a, b):
    return a + b

# Test klasy
@log(logging.DEBUG)
class Osoba:
    def __init__(self, imie):
        self.imie = imie

dodaj(5, 7)    
os = Osoba("Jan")