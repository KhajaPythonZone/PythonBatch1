def using_zip_demo():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    fruits = ["Apple", "Orange", "Banana", "Watermelon", "Pomegranate", "blueberry", "grapes"]
    drinks = ["coffee", "tea", "beer", "whiskey", "wine", "rum", "vodka"]
    count = len(days)
    index = 0
    for day, fruit, drink in zip(days, fruits, drinks):
        print(f"{day=} \n diet plan \n fruit = {fruit=} \n {drink=}")


def print_matrix_traditional():
    """
    This method will demonstrate creating a matrix
    """
    for row in range(1, 4):
        for col in range(1, 4):
            print(row, col)


def print_matrix_pythonic():
    """
    This method prints the matrix in a pythonic fashion
    :return:
    """
    rows = range(1, 4)
    cols = range(1, 4)
    cells = [(row, col) for row in rows for col in cols]
    for cell in cells:
        print(cell)
