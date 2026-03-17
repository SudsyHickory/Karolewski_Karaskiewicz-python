import sys

def print_sentences_max_4_words():

    sentence = ""
    end_of_lines_counter = 0

    while True:

        char = sys.stdin.read(1)

        if not char:
            if sentence.strip() != "":
                cleaned_sentence = " ".join(sentence.split())

                if count_words(cleaned_sentence) <= 4:
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

            if cleaned_sentence != "" and count_words(cleaned_sentence) <= 4:
                sys.stdout.write(cleaned_sentence + "\n")

                if end_of_lines_counter == 2:
                    sys.stdout.write("\n")

            sentence = ""
            end_of_lines_counter = 0


def count_words(sentence):
    words_counter = 0
    in_word = False

    for char in sentence:

        if char.isalpha():
            if not in_word:
                words_counter += 1
                in_word = True
        else:
            in_word = False

    return words_counter


def main():
    try:
        print_sentences_max_4_words()
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()