import sys

def get_sentences():
    sentence = ""
    end_of_lines_counter = 0

    while True:
        char = sys.stdin.read(1)
        if not char:
            if sentence.strip():
                yield sentence.strip()
            break

        if char == '\n':
            end_of_lines_counter += 1
            sentence += " "
        else:
            end_of_lines_counter = 0
            sentence += char
        

        if (char in ".?!") or (end_of_lines_counter == 2):
            cleaned = " ".join(sentence.split())
            has_letters = any(c.isalpha() for c in cleaned)
            
            if cleaned and has_letters:
                yield cleaned


            sentence = ""
            end_of_lines_counter = 0
            
def main():
    try:
        for s in get_sentences():
            sys.stdout.write(s + "\n")
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()
