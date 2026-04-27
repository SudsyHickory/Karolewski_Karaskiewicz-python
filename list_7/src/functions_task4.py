from functools import cache

def make_generator(f):

    #funkcja wewnetrzna
    def my_generator():
        n=1
        while True:
            yield f(n)      #yeild zwraca wartosc f(n) i zamraza stan funkcji do nastepnego wywolania
            n+=1
    return my_generator()     #wywolujemy funkcje wewnetrzna, aby zwrocic gotowy obiekt generatora

@cache      #do zadania 5, cache sprawi ze wyniki dla konkretnych n sa zapamietywane 
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
    
generator = make_generator(fib)


#an = a1 + (n-1)r
#f(n) = 5 + (n-1)r
gen_arithmetic = make_generator(lambda n: 5 +(n-1)*3)

#an = a1 * q^(n-1)
# f(n) = 2 * (3**(n-1))
gen_geometric = make_generator(lambda n: 2 * (3**(n - 1)))


print(next(generator)) #1
print(next(generator))  #1
print(next(generator))  #2
print(next(generator))  #3
print(next(generator))  #5

print(next(gen_arithmetic)) #5
print(next(gen_arithmetic)) #8
print(next(gen_arithmetic)) #11

print(next(gen_geometric))  #2
print(next(gen_geometric))  #6
print(next(gen_geometric)) #18