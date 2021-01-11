def iter_reverse_digits(number, base):
    while number != 0:
        digit = number % base
        yield digit
        number -= digit
        number //= base


def encode(alphabets, seed, size=6):
    if len(alphabets) < size:
        raise ValueError("There should be an alphabet per character you want")
    secret = "".join(
        alphabets[i][digit]
        for i, digit in enumerate(iter_reverse_digits(seed, len(alphabets[0])))
    )
    secret += "".join(alphabets[i][0] for i in range(len(secret), size))
    return secret
