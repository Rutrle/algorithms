def decimal_to_binary(number):
    if number == 0:
        return ''
    else:
        return decimal_to_binary(number//2) + str(number % 2)


def decimal_to_binary2(number, _result=""):
    if number == 0:
        return _result
    else:
        _result = str(number % 2) + _result
        return decimal_to_binary2(number//2, _result)


def decimal_to_binary2_wrap(number):
    return decimal_to_binary2(number)


def decimal_to_binary3(number):
    def decimal_to_binary2(number, _result=""):
        if number == 0:
            return _result
        else:
            _result = str(number % 2) + _result
            return decimal_to_binary2(number//2, _result)

    return decimal_to_binary2(number)


print(decimal_to_binary(1))
print(decimal_to_binary(233))


print(decimal_to_binary2(1))
print(decimal_to_binary2(233))
print(decimal_to_binary2_wrap(10))
print(decimal_to_binary3(10))
