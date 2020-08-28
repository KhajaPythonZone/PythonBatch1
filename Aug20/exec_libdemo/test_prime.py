class Prime:
    def __init__(self, number):
        self.number = number

    def is_prime(self):
        pass

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

    