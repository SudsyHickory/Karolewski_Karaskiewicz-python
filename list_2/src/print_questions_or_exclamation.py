import sys

def print_questions_or_exclamations():

    sentence = ""
    end_of_lines_counter = 0

    while True:

        char = sys.stdin.read(1)

        if not char:
            break

        if char == '\n':
            end_of_lines_counter += 1
            sentence += " "
        else:
            end_of_lines_counter = 0
            sentence += char

        if (char in ".?!") or (end_of_lines_counter == 2):
            cleaned_sentence = " ".join(sentence.split())
            
            if cleaned_sentence != "" and (char == '?' or char == '!'):
                sys.stdout.write(cleaned_sentence + "\n")

            sentence = ""
            end_of_lines_counter = 0


def main():
    try:
        print_questions_or_exclamations()
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()