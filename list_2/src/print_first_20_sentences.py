import sys

def print_first_20_sentences():

    sentence = ""
    end_of_lines_counter = 0
    sentences_counter = 0

    while True:

        char = sys.stdin.read(1)

        if not char:
            if sentence.strip() != "" and sentences_counter < 20:
                cleaned_sentence = " ".join(sentence.split())

                sys.stdout.write(cleaned_sentence + "\n")
            break

        if char == '\n':
            end_of_lines_counter += 1
            sentence += " "
        else:
            end_of_lines_counter = 0
            sentence += char

        if (char in ".?!") or (end_of_lines_counter == 2):
            cleaned_sentence = " ".join(sentence.split())

            if cleaned_sentence != "" and sentences_counter < 20:
                sys.stdout.write(cleaned_sentence + "\n")
                
                sentences_counter += 1

                if end_of_lines_counter == 2:
                    sys.stdout.write("\n")

            sentence = ""
            end_of_lines_counter = 0

            if sentences_counter >= 20:
                break


def main():
    try:
        print_first_20_sentences()
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()