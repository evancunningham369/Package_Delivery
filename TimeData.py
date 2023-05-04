# File holds all data related to keeping track of time
from datetime import timedelta

time_obj = timedelta(hours=8, minutes=0, seconds=0)


# resets the time to when the hub opens
def reset_time():
    global time_obj
    time_obj = timedelta(hours=8, minutes=0, seconds=0)


# gets the current time
def get_time():
    return time_obj


# adds to the current time
def add_time(time):
    global time_obj
    time_obj += time