class Quote:
    def __init__(self, person, words):
        """
        Initializer for quotes
        :param person: person
        :param words: words
        """
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def sayings(self):
        return self.words
