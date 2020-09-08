def echo(message):
    """
    This function will print the message
    :param message: messsage to be printed
    """
    print(message)


def describe_traffic_signal(color):
    """
    This functions returns textual meaning of traffic signals
    :param color: color of the traffic signal
    :return: message to be displayed and None for wrong color passed
    usage is
    message = describe_traffic_signal('red')
    if message:
         print(message)
    """
    if color == 'red':
        return "stop"
    elif color == "green":
        return "proceed"
    elif color == "orange":
        return "prepare to stop"
    else:
        return None


def whatis(thing):
    if thing or (thing == False):
        print("Its not none")
        print(f"Thing has some value: {thing}")
    else:
        print("None is passed")
