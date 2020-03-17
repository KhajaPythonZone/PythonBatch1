number1 = int(input("Enter starting number ")) 
number2 = int(input("Enter ending number ")) 
for number in range(number1,number2+1): 
    is_prime = True
    for index in range(2,number): 
        if number%index == 0:
            is_prime = False
            break
    if is_prime:
        print(number)