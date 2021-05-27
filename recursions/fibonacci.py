def fib(n):
    """
    return nth fibonacci element
    :param n: int
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1

    return fib(n-1)+fib(n-2)


def fib_list(n):
    """
    return list with fibonacci sequence up  to nth element
    :param n: int
    """
    if n == 1:
        fibonacci = [1]
        return fibonacci
    elif n == 2:
        fibonacci = [1, 1]
        return fibonacci

    fibonacci = fib_list(n-1)
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return fibonacci


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))

print(fib_list(7))
