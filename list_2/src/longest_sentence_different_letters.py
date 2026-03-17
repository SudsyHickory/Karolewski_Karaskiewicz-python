import sys

def get_longest_sentence_different_letters():

    longest_sentence_len = 0
    current_longest_sentence = ""
    sentence = ""
    char_counter = 0
    end_of_lines_counter = 0

    while True:

        char = sys.stdin.read(1)

        if not char:

            if char_counter > 0:
                cleaned_sentence = " ".join(sentence.split())

                if has_different_starting_letter(cleaned_sentence) and char_counter > longest_sentence_len:
                    current_longest_sentence = cleaned_sentence
                    longest_sentence_len = char_counter
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

            if has_different_starting_letter(cleaned_sentence) and char_counter > longest_sentence_len:
                current_longest_sentence = cleaned_sentence
                longest_sentence_len = char_counter

            char_counter = 0
            sentence = ""
            end_of_lines_counter = 0

    return current_longest_sentence


def has_different_starting_letter(sentence):

    previous_first_letter = ""

    for word in sentence.split():

        current_first_letter = ""

        for char in word:
            if char.isalpha():
                current_first_letter = char.lower()
                break

        if current_first_letter != "":
            if current_first_letter == previous_first_letter:
                return False
            previous_first_letter = current_first_letter

    return True


def main():
    try:
        sentence = get_longest_sentence_different_letters()
        if sentence:
            sys.stdout.write(sentence + "\n")
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()