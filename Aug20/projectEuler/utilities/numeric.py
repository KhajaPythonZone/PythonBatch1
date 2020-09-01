def is_divisible_by(number, factor):
    """
    This method will return true if the number is divisible by factor
    :param number: number
    :param factor: factor
    :return: true if divisible false other wise
    """
    return number % factor == 0


def is_prime(number):
    """
    This method will be used to determine if the number passed is prime
    or not
    :param number: number on which check has to be performed
    :return: true if prime false otherwise
    """
    is_prime_number = True
    for index in range((number//2)+1):
        if is_divisible_by(number, index):
            is_prime_number = False
            break
    return is_prime_number
