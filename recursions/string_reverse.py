def recursice_reversal(rec_string: str) -> str:
    if len(rec_string) == 0:
        return ''
    last_letter = rec_string[-1]
    rec_string = rec_string[:-1]
    return last_letter+recursice_reversal(rec_string)


print(recursice_reversal('tree'))
