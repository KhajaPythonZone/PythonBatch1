def square(x):
    return lambda: x * x


lamda_list = [square(number) for number in range(1, 10)]
for lambda_function in lamda_list:
    print(lambda_function())
