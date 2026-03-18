import sys
from common_tools import get_sentences

def get_longest_sentence_different_letters():

    longest_sentence = ""
    longest_sentence_len = 0

    for sentence in get_sentences():
        current_len = 0

        for char in sentence:
            if not char.isspace():
                current_len += 1

        if has_different_starting_letter(sentence) and current_len > longest_sentence_len:
                    longest_sentence = sentence
                    longest_sentence_len = current_len

    return longest_sentence


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