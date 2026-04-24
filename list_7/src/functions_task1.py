from functools import reduce

def acronym(words):

    return reduce(lambda acc, letter: acc + letter, map(lambda word: word[0].upper(), words), "") #[] na końcu - ustawienie pustego stringa jako wartość początkową akumulatora

def median(numbers):

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    return sorted_numbers[n // 2] if n % 2 != 0 else (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

def pierwiastek(x, epsilon):
    
    def step(y):
        return (y + x / y) / 2

    def next_step(y):
        return y if (y >= 0 and abs(y * y - x) < epsilon) else next_step(step(y))

    return next_step(x)

def make_alpha_dict(text):

    words = text.split()

    unique_letters = set(filter(lambda char: char != ' ', text))

    return {letter: list(filter(lambda word: letter in word, words)) for letter in unique_letters} #dla każdej litery tworzymy listę tylko tych słów, które zawierają tę literę

def flatten(lst):

    return reduce(lambda acc, element: acc + flatten(element) if isinstance(element, (list, tuple)) else acc + [element], lst, [])

def group_anagrams(words):

    def add_to_dict(acc, word):
        
        key = "".join(sorted(word))

        return {**acc, key: acc.get(key, []) + [word]} #**acc - kopiujemy akumulator, aby móc go zaktualizować

    return reduce(add_to_dict, words, {})

def main():

    print("1a: acronym")
    print(acronym(["Zakład", "Ubezpieczeń", "Społecznych"]))

    print("\n1b: median")
    print(median([1, 1, 19, 2, 3, 4, 4, 5, 1]))

    print("\n1c: pierwiastek")
    print(pierwiastek(3, epsilon=0.1))

    print("\n1d: make_alpha_dict")
    print(make_alpha_dict("on i ona"))

    print("\n1e: flatten")
    print(flatten([1, [2, 3], [[4, 5], 6]]))

    print("\n1f: group_anagrams")
    print(group_anagrams(["kot", "tok", "pies", "kep", "pek"]))

if __name__ == "__main__":
    main()