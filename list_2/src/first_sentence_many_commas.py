import sys
from common_tools import get_sentences

def get_first_sentence_many_commas():
    
    for sentence in get_sentences():
        
        commas_counter = 0

        for char in sentence:
            if char == ",":
                commas_counter += 1
            
        if commas_counter > 1:
            return sentence
    
    return ""

def main():
    try:
        sentence = get_first_sentence_many_commas()
        if sentence:
            sys.stdout.write(sentence + "\n")
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")
        
if __name__ == "__main__":
    main()