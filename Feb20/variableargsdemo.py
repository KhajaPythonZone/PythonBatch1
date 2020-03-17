def add(*args):
    print(f"Type of args is {type(args)} and value is {args} ")
    result = 0
    for arg in args:
        result += arg
    return result

def mul(**kwargs):
    print(f"Type of args is {type(kwargs)} and value is {kwargs} ")
    result = 1
    for name, value in kwargs.items():
        print(f"{name} = {value}")
        result *= value
    return result
        
#print(add(1))
#print(add(1,2))
#print(add(1,2,3,4,5,6,7,8,9))
print(mul(number1 = 1, number2 = 5))
print(mul(number1 = 1, number2 = 5, number3 = 10))