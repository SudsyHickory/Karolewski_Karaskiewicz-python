import sys

def get_sentences_with_proper_noun_procent():
    counter = 0
    total_sentences = 0

    end_of_lines_counter = 0
    is_in_sentence = False
    is_in_first_word = True
    is_in_word = False
    has_sentence_proper_noun = False

    while True:
        char = sys.stdin.read(1)
        if not char:
            if is_in_sentence:
                total_sentences+=1
                if has_sentence_proper_noun:
                    counter += 1
            break

        if(char == '\n'):
            end_of_lines_counter+=1
        else: 
            end_of_lines_counter=0
        
        if(char in ".?!") or (end_of_lines_counter==2):
            if is_in_sentence:
                total_sentences +=1
                if has_sentence_proper_noun:
                    counter += 1
            is_in_sentence = False
            is_in_first_word = True
            has_sentence_proper_noun = False
            is_in_word = False
            continue

        if(char.isalpha()):
            is_in_sentence = True
            if(not is_in_word):
                if(char.isupper()) and (not is_in_first_word):
                    has_sentence_proper_noun = True
                is_in_word = True
        else:
            if is_in_word:
                is_in_first_word = False
                is_in_word = False

    return counter, total_sentences

def main():
    try:
        count, total = get_sentences_with_proper_noun_procent()
        if total > 0:
            procent = (count / total) * 100
            sys.stdout.write(f"{procent:.2f}%\n")
        else:
            sys.stdout.write("0.00%\n")
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()
