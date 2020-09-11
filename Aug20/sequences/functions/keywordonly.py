def print_colors(colors, *, start=0, end=100):
    """
    This method is used to demonstrate named argumets
    :param colors: colors
    :param start: named argument start
    :param end:  named argument end
    """
    for color in (colors[start:end]):
        print(color, end=",")
    print()


if __name__ == "__main__":
    colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Violet', 'Indigo', 'White', 'Black']
    print_colors(colors)
    print("start=2 end =6")
    print_colors(colors, start=2, end=6)
    print("start=3")
    print_colors(colors, start=3)
    print("end = 5")
    print_colors(colors, end=5)
