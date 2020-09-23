def outer_function(arg1, arg2):
    def inner_function(arg3, arg4):
        return arg3 * arg4
    return inner_function(arg1, arg2)


if __name__ == "__main__":
    print(outer_function(4, 6))
