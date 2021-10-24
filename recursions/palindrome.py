def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return True and is_palindrome(string[1:-1])
    else:
        return False


print(is_palindrome('kajak'))
print(is_palindrome('ksjak'))
