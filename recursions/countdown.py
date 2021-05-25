def countdown(starting_number):
    """
    recursive function for counting down from given number
    :param starting_number: positive int
    """
    if starting_number <= 0:
        print(0)
        return None

    print(starting_number)
    countdown(starting_number-1)


countdown(10)