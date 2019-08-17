# This week, we're going to enter the world of decorators. Decorators allow us to capture a function (or class) when it is being defined, as well as when it's being called, and do ... well, whatever we want with it. It's hard to exaggerate just how powerful decorators can be.

# This week, we're going to write a decorator that stops us from running a function too often. The decorator, which we'll call "once_per_minute", will restrict a decorated function from being called more often than (you guessed it) once per minute.

# If you try to invoke the function too soon, then you'll raise a TooSoonError exception, whose message tells you how much longer you need to wait.

# For example, given the following code:
#     @once_per_minute
#     def hello(name):
#         return "Hello, {}".format(name)

#     for i in range(30):
#         print(i)
#         try:
#             time.sleep(3)
#             print(hello("attempt {}".format(i)))
#         except TooSoonError as e:
#             print("Too soon: {}".format(e))

# The above will print something like:
#     0
#     Hello, attempt 0
#     1
#     Too soon: Wait another 56.997233867645264 seconds
#     2
#     Too soon: Wait another 53.99469590187073 seconds
#     3
#     Too soon: Wait another 50.99368476867676 seconds
#     4
#     Too soon: Wait another 47.99025297164917 seconds
#     5
#     Too soon: Wait another 44.9868860244751 seconds

# When we finally get to i = 20, then it'll run the function.  But it'll also reset the clock at that point, waiting another 60 seconds until we can invoke the function again.

# The decorator should handle the fact that a decorated function might take any number or type of parameters.

import functools
from datetime import datetime, timedelta

next_run_times = {}

def once_per_minute(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        now = datetime.now()
        global next_run_times
        if func.__name__ in next_run_times and next_run_times[func.__name__] > now:
            raise TooSoonError(f"Too Soon, try again in: {next_run_times[func.__name__] - now}")
            return


        # Do something before
        value = func(*args, **kwargs)
        next_run_times[func.__name__] = now + timedelta(seconds=60)
        # Do something after
        return value
    return wrapper_decorator

class TooSoonError(Exception):
    message = "AuthorizerError"