import sys

def get_first_sentence_many_commas():

    sentence = ""
    commas_counter = 0
    end_of_lines_counter = 0

    while True:

        char = sys.stdin.read(1)

        if not char:
            if commas_counter > 1:
                return " ".join(sentence.split())
            break

        if char == '\n':
            end_of_lines_counter += 1
            sentence += " "
        else:
            end_of_lines_counter = 0
            sentence += char

        if char == ',':
            commas_counter += 1

        if (char in ".?!") or (end_of_lines_counter == 2):
            cleaned_sentence = " ".join(sentence.split())
            
            if commas_counter > 1:
                return cleaned_sentence

            sentence = ""
            commas_counter = 0
            end_of_lines_counter = 0

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