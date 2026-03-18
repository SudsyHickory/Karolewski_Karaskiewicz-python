import sys
from common_tools import get_sentences, print_sentences

def get_first_20_sentences():

    sentences_counter = 0

    for sentence in get_sentences():

        if sentences_counter < 20:
            yield sentence
            sentences_counter += 1
        else:
            break

def main():
    try:
        print_sentences(get_first_20_sentences())
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()