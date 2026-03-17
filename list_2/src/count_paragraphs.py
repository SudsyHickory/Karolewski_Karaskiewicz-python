import sys

def get_count_paragraphs():
    count = 0
    newlines_in_a_row = 0
    in_paragraph = False 

    while True:
        char = sys.stdin.read(1)

        if not char:
            if in_paragraph:
                count +=1 
            break

        if char == "\n":
            newlines_in_a_row +=1 
            if newlines_in_a_row == 2 and in_paragraph:
                count+=1
                in_paragraph=False
        elif char.strip():
            in_paragraph = True
            newlines_in_a_row = 0
    
    return count

def main():
    try:
        result = get_count_paragraphs()
        sys.stdout.write(str(result) + '\n')
    except Exception as e:
        sys.stderr.write(f"Blad: {e} \n")

if __name__ == "__main__":
    main()