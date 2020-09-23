def is_prime(number):
    """
    This method will print if the number is prime
    :param number:
    :return: True when prime False otherwise
    """
    is_prime_flag = True
    for index in range(2, number // 2):
        if number % index == 0:
            is_prime_flag = False
            break
    return is_prime_flag


def is_even(number):
    """
    This method will check if the number is even or odd
    :param number: number to be checked
    :return: True if even, False otherwise
    """
    return number % 2 == 0

def print_exam_outcome(marks, total=100):
    """
    This method will print the grades
    grade A > 80%
    grade B > 60%
    grade C < 60%

    :param marks: marks obtained
    :param total: total marks
    :return: grade
    """
    percentage = (marks/total)*100
    if percentage > 80:
        return "A"
    elif percentage > 60:
        return "B"
    else:
        return "C"


if __name__ == '__main__':
    in_number = int(input("Enter any number "))
    if is_prime(in_number):
        print(f"The {in_number} is prime")
