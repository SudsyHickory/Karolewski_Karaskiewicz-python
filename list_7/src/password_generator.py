import string
import random

class PasswordGenerator:

    def __init__(self, length, charset=string.ascii_letters + string.digits, count=10):
        self.length = length
        self.charset = charset
        self.count = count
        self.generated = 0 #licznik wygenerowanych haseł

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.generated >= self.count:
            raise StopIteration
        
        password = "".join(random.choices(self.charset, k=self.length)) #random.choices - losuje length znaków ze zbioru charset

        self.generated += 1

        return password

def main():

    print("Test z jawnym wywołaniem next():")

    generator = PasswordGenerator(length=10, count=3)

    print(next(generator))
    print(next(generator))
    print(next(generator))

    try:
        print(next(generator))
    except StopIteration:
        print("Wygenerowano już wszystkie hasła")

    print("\nTest w pętli for:")

    for password in PasswordGenerator(length=10, count=5):
        print(password)

if __name__ == "__main__":
    main()