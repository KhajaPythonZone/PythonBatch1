class Credentials:
    """
    Credentials class to hold username & password
    """

    def __init__(self, username='admin', password='admin@123'):
        """
        initilzation of credentials
        :param username: username
        :param password: password
        """
        self._username = username
        self._password = password

    def username(self):
        """
        Username access property
        :return: username
        """
        return self._username

    def password(self):
        """
        Password access property
        :return: password
        """
        return self._password


class SecretString:
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """
        Only decrypt if the pass_phrase is matching
        :param pass_phrase:
        :return:
        """
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""
