def is_prime(number):
    # This function will return true if the number is prime, false otherwise
    is_prime_number = True
    for index in range(2,(number//2+1)):
        if number%index == 0:
            is_prime_number = False
            break
    return is_prime_number

def largest_prime_factor(number):
    # This function returns largest prime factor
    for index in range(number//2,2,-1):
        if number%index == 0 and is_prime(index):
            return index

print(largest_prime_factor(600851475143))

    
