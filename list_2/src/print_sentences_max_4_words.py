import sys
from common_tools import get_sentences, print_sentences

def get_sentences_max_4_words():

    for sentence in get_sentences():
        if count_words(sentence) <= 4:
            yield sentence

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
        print_sentences(get_sentences_max_4_words())
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()