import sys
from count_status_classes import count_status_classes
from get_top_uris import get_top_uris
from get_top_ips import get_top_ips
from get_extension_stats import get_extension_stats
from common_tools import *
from get_unique_methods import get_unique_methods
from detect_sus import detect_sus

def analyze_log(log):
    report = {
        "status_classes" : count_status_classes(log),
        "top_uris" :  get_top_uris(log,5),
        "top_ips" :  get_top_ips(log),
        "extensions" : get_extension_stats(log),
        "methods": get_unique_methods(log),
        "sus_ips" : detect_sus(log,2000)
    }
    return report


def main():
    try:
        
        log = read_log()
        
        if not log:
            print("Brak danych do analizy.")
            return

        
        report = analyze_log(log)

        print("="*40)
        print("       RAPORT Z ANALIZY LOGÓW")
        print("="*40)

        
        # Rozkład kodów statusu
        print("Rozkład klas statusu:")
        status_stats = report.get('status_classes', {})
        for s_class, count in status_stats.items():
            print(f"  {s_class}: {count}")
        print("-" * 20)
        

        # Rodzaje metod
        print("Rodzaje metod:")
        methods_stats = report.get('methods', {})
        for method in methods_stats:
            sys.stdout.write(method + "\n")
        print("-" * 20)

        # Najaktywniejsze IP 
        if 'top_ips' in report and report['top_ips']:
            ip_tuple = report['top_ips'][0]
            print(f"Najaktywniejszy adres IP: {ip_tuple[0]} (liczba: {ip_tuple[1]})")
        print("-" * 20)

        # Najaktywniejsze URI
        if 'top_uris' in report and report['top_uris']:
            uri_tuple = report['top_uris'][0]
            print(f"Najaktywniejsze URI: {uri_tuple[0]} (liczba: {uri_tuple[1]})")
        print("-" * 20)

        # Rozszerzenia plików
        print("Najczęstsze rozszerzenia plików:")
        ext_stats = report.get('extensions', {})
        
        # Sort i 5 pierwszych
        sorted_ext = sorted(ext_stats.items(), key=lambda x: x[1], reverse=True)[:5]
        
        for ext, count in sorted_ext:
            print(f"  .{ext:<10} : {count}")
        
        print("="*40)

        #Podejrzane adresy IP
        print("Podejrzane adresy ip:")
        suspects = report.get('sus_ips', {})
        for ip in suspects:
            print(f" - {ip}")
        print("-" * 20)

    except Exception as e:
        sys.stderr.write(f"Wystąpił błąd podczas generowania raportu: {e}\n")

if __name__ == "__main__":
    main()