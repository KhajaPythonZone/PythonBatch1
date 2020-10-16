from ducktyping import quote

class Question(quote.Quote):

    def sayings(self):
        return f"{self.words}?"

class Exclamation(quote.Quote):

    def sayings(self):
        return f"{self.words}!"