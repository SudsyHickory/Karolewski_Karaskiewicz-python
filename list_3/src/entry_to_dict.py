from common_tools import *

#import funkcji z common_tools
def main():
    try:
        log = read_log()
        dict = entry_to_dict(log[1])

        for name, value in dict.items():
            sys.stdout.write(str(name)  + " " + str(value) + "\n")

    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()