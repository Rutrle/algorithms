def fibonacci(num):
    if num <= 2:
        return 1
    return fibonacci(num-1)+fibonacci(num-2)


print(fibonacci(5))


    