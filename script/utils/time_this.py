
def time_this(original_function):
    def new_function(*args, **kwargs):
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("{0} - Elapsed Time = {0}".format(original_function.__name__, after-before))
        return x
    return new_function
