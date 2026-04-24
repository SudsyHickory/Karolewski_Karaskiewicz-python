from itertools import islice

def forall(pred, iterable):

    return all(map(pred, iterable))

def exists(pred, iterable):

    return any(map(pred, iterable))

def atleast(n, pred, iterable):

    return sum(1 for _ in islice(filter(pred, iterable), n)) == n #islice - zatrzyma działanie filtra gdy zostanie już znaleziony n-ty element

def atmost(n, pred, iterable):

    return sum(1 for _ in islice(filter(pred, iterable), n + 1)) <= n

def main():

    parzyste = lambda x: x % 2 == 0

    liczby1 = [2, 4, 6, 8, 10]
    liczby2 = [1, 3, 4, 7, 9]
    
    print("2a: forall")
    print(forall(parzyste, liczby1))
    print(forall(parzyste, liczby2))

    print("\n2b: exists")
    print(exists(parzyste, liczby1))
    print(exists(parzyste, liczby2))

    print("\n2c: atleast")
    print(atleast(3, parzyste, liczby1))
    print(atleast(2, parzyste, liczby2))
    print(atleast(1, parzyste, liczby2))

    print("\n2d: atmost")
    print(atmost(3, parzyste, liczby1))
    print(atmost(2, parzyste, liczby2))

if __name__ == "__main__":
    main()