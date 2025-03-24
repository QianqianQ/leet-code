from typing import Iterator


def fibonacchi_loop(n: int) -> list[int]:
    '''
    This function returns the first n fibonacci numbers using loop.
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    prev1 = 0
    prev2 = 1
    fibonacci_array = [prev1, prev2]

    for i in range(n):
        newFibo = prev1 + prev2
        fibonacci_array.append(newFibo)
        prev1 = prev2
        prev2 = newFibo

    return fibonacci_array

# print(fibonacchi_loop(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def fibonacchi_recursive(n: int) -> list[int]:
    '''
    This function returns the first n fibonacci numbers using recursion.
    Time complexity: O(2^n)
    Space complexity: O(n)
    '''
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    fibo = fibonacchi_recursive(n-1)
    fibo.append(fibo[-1] + fibo[-2])
    return fibo


def fibonacchi_recursive_memo(n: int, memo: dict[int, int] = {}) -> list[int]:
    '''
    This function returns the first n fibonacci numbers using recursion with memoization.
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    if n in memo:
        return memo[n]
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    fibo = fibonacchi_recursive_memo(n-1, memo)
    fibo.append(fibo[-1] + fibo[-2])
    memo[n] = fibo
    return fibo


def fib(n: int) -> Iterator[int]:
    '''
    This function returns the first n fibonacci numbers using generator.
    Time complexity: O(n)
    Space complexity: O(1)
    '''
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
    # prev1 = 0
    # prev2 = 1
    # yield prev1
    # yield prev2

    # for i in range(n):
    #     newFibo = prev1 + prev2
    #     yield newFibo
    #     prev1 = prev2
    #     prev2 = newFibo
