def fib(n):
    """
    returns nth number of fibonacci sequence
    : param n: int
    """

    if n == 1 or n == 2:
        return 1

    else:
        return fib(n-1) + fib(n-2)


print(fib(6))
