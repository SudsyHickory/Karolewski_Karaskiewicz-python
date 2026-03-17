import sys

def get_longest_sentence():
   
    longest_sentence_len = 0
    current_longest_sentence = ""
    sentence = ""
    char_counter = 0
    end_of_lines_counter = 0

    while True:
        char = sys.stdin.read(1)
        if not char:
            if char_counter > longest_sentence_len:
                current_longest_sentence = sentence
            break

        if char == '\n':
            end_of_lines_counter += 1
            sentence += " "
        else:
            end_of_lines_counter = 0
            sentence += char
        
        if not char.isspace():
            char_counter += 1

        if (char in ".?!") or (end_of_lines_counter == 2):
            cleaned_sentence = " ".join(sentence.split())
            
            if char_counter > longest_sentence_len:
                current_longest_sentence = cleaned_sentence
                longest_sentence_len = char_counter
            
            char_counter = 0
            sentence = ""
            end_of_lines_counter = 0
            continue

    return current_longest_sentence

def main():
    try:
        najdluzsze = get_longest_sentence()
        if najdluzsze:
            sys.stdout.write(najdluzsze + "\n")
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()
