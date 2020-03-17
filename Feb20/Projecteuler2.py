# assign number1 and number2
number1 = 1
number2 = 2
max = 4000000
# print(number1)
# print(number2)
result = 0
sum = 2
while result < max:
	result = number1 + number2
	if result < max:
		# print(result)
		if result%2 == 0:
			sum += result
	number1 = number2
	number2 = result
print(f"sum of even valued fibonnaci series below {max} is {sum}")