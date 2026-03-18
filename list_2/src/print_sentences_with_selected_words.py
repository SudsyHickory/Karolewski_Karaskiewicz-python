import sys
from common_tools import get_sentences, print_sentences

def get_sentences_with_selected_words():

    for sentence in get_sentences():
        if count_selected_words(sentence) >= 2:
            yield sentence

def count_selected_words(sentence):

    selected_words_counter = 0
    word = ""

    for char in sentence:

        if char.isalpha():
            word += char.lower()
        else:
            if is_selected_word(word):
                selected_words_counter += 1
                
            word = ""

    if is_selected_word(word):
        selected_words_counter += 1

    return selected_words_counter

def is_selected_word(word):
    return (word == "i" or word == "oraz" or word == "ale" or word == "że" or word == "lub")

def main():
    try:
        print_sentences(get_sentences_with_selected_words())
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()