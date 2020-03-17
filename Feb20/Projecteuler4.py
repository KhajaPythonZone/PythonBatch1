number1 = 99
number2 = 99
pallendromes = []
while number1 > 9:
    while number2 > 9:
        number = number1 * number2
        temp_number = number
        reverse = 0
        while temp_number > 0:
            reverse = temp_number%10 + (reverse * 10)
            temp_number = temp_number//10
        if reverse == number:
            print(f"{number} is pallendrome")
            pallendromes.append(number)
        number2 = number2 -1
    number1 = number1 -1

# sort pallendromes and largest index is largest pallendrome
pallendromes.sort()
largest = pallendromes[len(pallendromes) -1]
print(f"Largest pallendrome is {largest} ")

    
    
