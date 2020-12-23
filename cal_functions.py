# Created by wfletch.

# This module holds static functions to be used for the creation of a calendar.
import math

calander = {
    "Monday": {},
    "Tuesday": {},
    "Wednesday": {},
    "Thursday": {},
    "Friday": {},
    "Saturday": {},
    "Sunday": {}
}
TIME_DELTA = 30
def day_task_from_until(day, start, end, task):
    time_intervals = get_time_intervals()
    s = None
    e = None
    i = 0
    for delta_time in time_intervals:
        if delta_time == start:
            s = i
        if delta_time == end:
            e = i
            break
        i+=1
    for i in range(s, e + 1, 1):
        calander[day][time_intervals[i]] = task

def everyday_task_from_until(start, end, task):
    for k in calander.keys():
        day_task_from_until(k,start,end,task)


def get_time_intervals():
    time_intervals = [None] * 48
    for i in range(0, 48, 1):
        temp_time = ""
        if (i < 20):
            temp_time += "0"
        temp_time += str(int(math.floor(i / 2)))
        temp_time += ":"
        if (i % 2 == 0):
            temp_time += "00"
        else:
            temp_time += "30"
        time_intervals[i] = temp_time
    return time_intervals

def get_day(day):
    return calander[day]

for k in calander.keys():
    day_task_from_until(k, "00:00", "23:30", "Free")

def get_free_time_for_day(day):
    free_time = []
    for t_slot in (calander[day].keys()):
        if (calander[day][t_slot]  == "Free"):
            free_time.append(t_slot)
    return free_time

def count_free_time_for_day(day):
    free_time = get_free_time_for_day(day)
    free_minutes =  len(free_time) * TIME_DELTA
    #TODO: Return as DateTime: X Hours and Y Minutes
    #free_hours = math.floor(free_minutes / 60)
    return free_minutes


def clear_day(day):
    for t_slot in (calander[day].keys()):
        calander[day][t_slot]  = "Free"
