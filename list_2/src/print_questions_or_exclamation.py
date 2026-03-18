import sys
from common_tools import get_sentences, print_sentences

def get_questions_or_exclamations():

    for sentence in get_sentences():
        if sentence.endswith("?") or sentence.endswith("!"):
            yield sentence

def main():
    try:
        print_sentences(get_questions_or_exclamations())
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()