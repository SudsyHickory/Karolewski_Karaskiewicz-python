import sys

def get_non_white_char_count():

    count = 0
    while True:
        char = sys.stdin.read(1)
        if not char:
            break
        elif char.strip():
            count +=1
    return count

def main():
    try:
        result = get_non_white_char_count()
        sys.stdout.write(str(result) + "\n")
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()