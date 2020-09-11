
def pig_latin(word):
    """
    This method will return the pig latin word
    :param word: word to be encrypted to pig_latin
    :return: word encrypted to pig_latin
    """
    if word[0] in 'aeiou':
        return f"{word}way"

    return f"{word[1:]}{word[0]}ay"


def pig_latin_sentence(sentence):
    """
    This method will return the pig latin word
    :param sentence: sentence to be encrypted to pig_latin
    :return: sentence encrypted to pig_latin

    """
    output = []
    for word in sentence.split():
        output.append(pig_latin(word))

    return ' '.join(output)
