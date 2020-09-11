def run_anything(func):
    """
    Pass any function to it
    :param func: function
    :return:
    """
    func()


def pi():
    """
    This function prints pi
    :return:
    """
    print('3.14')


if __name__ == "__init__":
    run_anything(pi)
