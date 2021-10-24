def decimal_to_binary(number):
    if number == 0:
        return ''
    else:
        return str(number % 2) + decimal_to_binary(number//2)


def decimal_to_binary2(number, _result=""):
    if number == 0:
        return _result
    else:
        _result = _result + str(number % 2)
        return decimal_to_binary2(number//2, _result)


print(decimal_to_binary(1))
print(decimal_to_binary(233))


print(decimal_to_binary2(1))
print(decimal_to_binary2(233))
