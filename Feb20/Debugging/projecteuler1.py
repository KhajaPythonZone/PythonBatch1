def project_euler_1(max_number, number1=3, number2=5):
    # This function has two default arguments number1 and number2
    # if you pass the value the value will be overwritten, if you dont pass the 
    # value, This functions takes default
    # example: project_euler_1(1000,5,3) => number1=> 5, number2 = 3
    # project_euler_1(1000) => number1 => 3, number2 => 5

    result = 0
    for index in range(1,max_number):
        is_divisible = (index%number1 == 0 or index%number2 ==0)
        if is_divisible:
            result = result+index
    return result

print(project_euler_1(1000))