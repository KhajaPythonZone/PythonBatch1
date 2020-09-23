def prettify(msg):
    """
    This method will capitalize the string
    :return:
    """

    def cap_message():
        return msg.capitalize()

    return cap_message


if __name__ == "__main__":
    message = input("Enter the message")
    prettify_func = prettify(message)
    print(prettify_func())
