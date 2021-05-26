def fact(num):
    """
    returns recursively calculated factorial

    """

    if num > 0:
        return num*fact(num-1)
    if num == 0:
        return 1


print(fact(10))
