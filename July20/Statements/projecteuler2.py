value_1 = 1
value_2 = 2
result = 2
sum = 0
while value_1 + value_2 <= 4000000:
    sum = value_1 + value_2
    if sum%2 == 0:
        result = result + sum
    value_1 = value_2
    value_2 = sum
print(result)