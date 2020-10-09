import datetime

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def trace(func):
    def print_trace(*args, **kwargs):
        print(f"Inputs passed for {func} are {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"output of the function is {result}")
    return print_trace

def in_days(func):
    def day_in_words(*args):
        day_in_number = func(*args)
        return days[day_in_number]
    return day_in_words

@trace
@in_days
def day_of_week(input_date = datetime.datetime.today()):
    """
    This method will return the day of the week
    """
    return input_date.weekday()

@trace
def add(*args):
    """
    This function will add arguments
    """
    return sum(args)


if __name__ == "__main__":
    print(f"Today is {day_of_week()}")
    indian_independence_date = datetime.datetime(year=1945, month=8, day=15)
    print(f"Independence day was on {day_of_week(indian_independence_date)}")
    add(1,2)
    add(1,2,3,4,5,6,7,8,9,10,11,12)
