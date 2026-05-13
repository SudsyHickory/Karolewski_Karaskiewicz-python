from functools import cache
from functions_task4 import make_generator, fib
import time

def make_generator_mem(f):

    memoized_f = cache(f)       #tworzymy funkcje f, ktora posiada slownik wynikow, wiec wywolanie dla tego samego argumentu n bedzie natychmiastowe
    return make_generator(memoized_f)


generator = make_generator_mem(fib)

start = time.time()

for _ in range(37):
    print(next(generator))

end = time.time()

print(f"Took {end - start:.4f} seconds")


