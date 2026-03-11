from time import time


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = 30
    start_time = time()
    result = fib(n)
    end_time = time()
    print(
        f"Fibonacci of {n} is {result}. Computation took {end_time - start_time:.4f} seconds."
    )
