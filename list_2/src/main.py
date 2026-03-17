import sys
import io

def exc2():
    in_preamble = True
    lines_number = 0
    empty_lines = 0
    
    for line in sys.stdin:
        
        lines_number +=1

        if(line.startswith("-----")):
            break

        if in_preamble:
            if line.strip() == "":
                empty_lines +=1
            else:
                empty_lines = 0
            
            if empty_lines>=2 and lines_number<= 10:
                in_preamble = False
                continue
            if lines_number> 10:
                in_preamble = False
            else:
                continue
       
        processed_line = " ".join(line.split())
        if processed_line == "":
            print("")
        else:
            print(processed_line)

def main():
    
    try:
        exc2() 
    except Exception as e:
        sys.stderr.write(f"Błąd: {e}\n")

if __name__ == "__main__":
    main()

# chcp 65001
#type plik.txt | python twoj_skrypt.py