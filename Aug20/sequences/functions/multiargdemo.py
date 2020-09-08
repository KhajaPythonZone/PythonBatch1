def multiple_args(args=[]):
    """
    Passing a list to the function
    :param args:
    :return:
    """
    for arg in args:
        print(arg)


def variable_arguments(*args):
    """
    This function supports passing multiple arguments
    :param args: arguments
    :return:
    """
    print(args)
    print(f"the type of args is {type(args)}")


def add(*args):
    """
    This method will add the arguments
    :param args: arguments
    :return: sum of arguments
    """
    result = 0
    for arg in args:
        result += arg
    return result


def join_string(symbol, *args):
    """
    This method will join the string with the args passed
    :param symbol: symbol to be used
    :param args: arguments
    :return:
    """
    result = symbol.join(args)
    return result


if __name__ == "__main__":
    # multiple_args(['red', 'blue', 'green'])
    print(join_string("  ", 'hello', 'how are you'))
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))
