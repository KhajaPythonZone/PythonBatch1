class Prime:
    def __init__(self, number):
        self.number = number

    def is_prime(self):
        is_prime_number = True
        index = 2
        while(index < self.number//2):
            if self.number%index == 0:
                is_prime_number = False
                break
            index = index+1
        return is_prime_number

def main():
    value = 11
    prime = Prime(value)
    if prime.is_prime():
        print("Prime number")
    else:
        print("Not a prime")



if __name__ == "__main__":
    # This module is executed directly 
    main()

    