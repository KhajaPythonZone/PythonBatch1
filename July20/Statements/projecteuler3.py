number = 600851475143
factor = number//2
while factor > 1:
    if number%factor == 0:
        # This means it is a factor
        # now check if this factor is prime
        is_prime_factor = True
        index = 2
        while index <= factor//2:
            if factor%index == 0:
                is_prime_factor = False
                break
            index = index + 1
        if is_prime_factor == True:
            print(factor)
            exit(0)
    factor = factor -1
            