is_factor = lambda x, y: x % y == 0


def prime_factors(value=13195):
    """
    In this method will try to find prime factors
    """
    prime_factors_found = [index for index in range(2, value//2) if is_factor(value, index) and is_prime(index)]
    return prime_factors_found


def is_prime(value):
    is_prime_number = True
    for index in range(2, value//2):
        if is_factor(value, index):
            is_prime_number = False
            break
    return is_prime_number
