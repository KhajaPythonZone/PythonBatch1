def traditional_solution(max_number=10):
    """
    In this method lets look at traditional solution for project euler problem 1
    https://projecteuler.net/problem=1
    """
    result = 0
    for index in range(1, max_number):
        if index % 3 == 0 or index % 5 == 0:
            result += index
    return result


def list_comprehension_solution(max_number=10):
    multiples = [index for index in range(1, max_number) if index % 3 == 0 or index % 5 == 0]
    # conditions can be placed in the front as well
    # multiples = [index if index % 3 == 0 or index % 5 == 0 else 0 for index in range(1, max_number) ]
    return sum(multiples)
