# fibonacci_multiprocessing.py

import multiprocessing

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    # for _ in range(multiprocessing.cpu_count()):
    #     multiprocessing.Process(target=fib, args=(35,)).start()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(fib, range(40))
        for i, result in enumerate(results):
            print(f"fib({i}) = {result}")