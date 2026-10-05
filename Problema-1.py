import time

def function(n):
    counter = 0
    i = n // 2
    while i <= n:
        j = 1
        while j + n // 2 <= n:
            k = 1
            while k <= n:
                counter += 1
                k *= 2
            j += 1
        i += 1
    return counter

for n in [1, 10, 100, 1000, 10000, 100000]:
    start = time.perf_counter()
    function(n)
    end = time.perf_counter()
    print(f"n={n}, time={end-start:.6f}s")