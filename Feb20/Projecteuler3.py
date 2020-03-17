# This program accepts input from user and displays 
# whether the input is prime or not
number = int(input("Enter any number of your choice "))
for factor in range(number,2,-1):
    if number%factor == 0:
        # seems like a factor
        # now let me check if it is prime or not
        is_prime = True
        for index in range(2,factor):
            if factor%index == 0:
                is_prime = False
                break
        if is_prime:
            print (f"largest prime factor of {number} is {factor}")
            exit(0)
    






    