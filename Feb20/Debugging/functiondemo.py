def log_message():
    print('nonsense')

def add(number1, number2):
    # This function adds the two numbers
    print(f'attempting to add {number1} and {number2}')
    log_message()
    return number1 + number2

result = add(3,5)
print(result)