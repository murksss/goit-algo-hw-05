from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        """
        :param n: the serial number of the n-th Fibonacci number
        :return: the value of the n-th Fibonacci number
        """
        if n < 0:
            print('The serial number must be positive')
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


if __name__ == '__main__':
    get_fibonacci = caching_fibonacci()

    print(get_fibonacci(10))
    print(get_fibonacci(6))
