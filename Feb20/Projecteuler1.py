extra_checks = (input('Enter 1 for checks 0 for no checks') == '1')
max_number = 10
number1 = 3
number2 = 5
result = 0
for index in range(1,max_number):
    if extra_checks:
        print('checking for index = '+str(index))
    is_divisible = (index%3 == 0 or index%5 ==0)
    if extra_checks:
        print('is_divisble by 3 or 5 = '+str(is_divisible))
    if is_divisible:
        result = result + index	
    if extra_checks:
        print('result so far = '+str(result))
print(result)