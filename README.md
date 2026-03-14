# Karolewski & Karaśkiewicz: Python Project

## 👥 Skład zespołu
* **Jakub Karolewski**
* **Jakub Karaśkiewicz**

## 🎯 Cel projektu
Celem projektu jest stworzenie funkcjonalnej aplikacji w języku Python przy jednoczesnym doskonaleniu umiejętności współpracy zespołowej. Projekt koncentruje się na praktycznym wykorzystaniu:

* **Systemu kontroli wersji Git:** Zarządzanie historią zmian.
* **Git Flow:** Praca na gałęziach (*feature branches*) i proces *Pull Request*.
* **Code Review:** Wzajemna weryfikacja kodu w celu zapewnienia wysokiej jakości.
* **Testowanie:** Implementacja testów dla kluczowych modułów.

---

## 📂 Struktura projektu
Repozytorium zostało zorganizowane zgodnie z najlepszymi praktykami:

| Katalog | Opis zawartości |
| :--- | :--- |
| `src/` | Kod źródłowy aplikacji (logika biznesowa) |
| `tests/` | Testy |
| `docs/` | Dokumentacja techniczna i projektowa |

---

## 🛠 Instrukcja uruchomienia
Aby uruchomić projekt lokalnie, wykonaj poniższe kroki:

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/SudsyHickory/Karolewski_Karaskiewicz-python.git
2. Zainstaluj zależności:
    ```bash
   pip install -r requirements.txt
3. Uruchom program główny:
    ```bash
    python src/main.py
---

## 📊 Podsumowanie współpracy i podział ról

### 👤 Kto za co odpowiadał:

* **Jakub Karolewski:**
    * Inicjalizacja i konfiguracja repozytorium na platformie GitHub.
    * Opracowanie kompletnej dokumentacji projektu oraz przygotowanie pliku `README.md`.
* **Jakub Karaśkiewicz:**
    * Zaprojektowanie architektury kodu źródłowego wewnątrz `src/main.py`.
    * Implementacja warstwy testowej i dbałość o poprawność działania algorytmów.

---

### 💡 Kluczowe wnioski i nabyte umiejętności:

Podczas realizacji projektu nie tylko stworzyliśmy działającą aplikację, ale przede wszystkim zgłębiliśmy dobre praktyki inżynierii oprogramowania:

1.  **Standardy organizacji kodu:** Nauczyliśmy się, jak profesjonalnie separować logikę biznesową od testów poprzez poprawną strukturę katalogów (`src/`, `tests/`).
2.  **Modularność w Pythonie:** Opanowaliśmy techniki poprawnego importowania modułów między folderami, co jest kluczowe przy skalowaniu projektów.
3.  **Zaawansowany Git Flow:** W praktyce przećwiczyliśmy pełny cykl życia zmiany w kodzie – od pracy na izolowanych gałęziach (*branches*), przez synchronizację lokalnych środowisk (`fetch`/`pull`), aż po profesjonalny proces **Code Review** w ramach *Pull Requestów* przed ostatecznym scaleniem zmian.