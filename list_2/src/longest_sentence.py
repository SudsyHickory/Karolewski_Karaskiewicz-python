import sys
from common_tools import get_sentences

def get_longest_sentence():
   
    longest = ""

    for s in get_sentences():
        if len(s) > len(longest):
            longest = s
            
    return longest

def main():
    try:
        result = get_longest_sentence()
        if result:
            sys.stdout.write(result + "\n")
    except Exception as e:
        sys.stderr.write(f"Blad: {e}\n")

if __name__ == "__main__":
    main()
