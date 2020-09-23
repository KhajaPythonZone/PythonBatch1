def decorate_word(word):
    """
    We decorate the word by capitalizing and adding ! at the end
    :param word: word to be decorated
    :return: <Word!>
    """
    return f"{word.capitalize()}!"


def rename_heros(superheros):
    """
    :param superheros:
    :return:
    """
    for superhero in superheros:
        my_func = lambda hero: f"{hero.capitalize()}!"
        print(my_func(superhero))


if __name__ == "__main__":
    rename_heros(['ironman', 'thor', 'hulk'])
