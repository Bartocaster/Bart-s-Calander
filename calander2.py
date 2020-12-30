 # Created by B. Huiskamp.

import pprint
import cal_functions as cal # cal_functions is the name of the library. We are aliasing it as cal


pp = pprint.PrettyPrinter(indent=4)


# Populate All Days

# cal is referencing the cal_functions library (We alias cal_functions as cal)
cal.everyday_task_from_until("00:00", "06:00", "Sleep")
cal.everyday_task_from_until("22:00", "23:30", "Sleep")
cal.everyday_task_from_until("06:30", "17:00", "Work")
cal.everyday_task_from_until( "17:30", "17:30", "Rest")
cal.everyday_task_from_until( "19:00", "19:30", "dinner")



#figure out how to make friday diffrent
# cal.day_task_from_until('Friday', '16:00', '18:00', 'Fuck All')


# TODO: Set Up Saturday and Sunday

print("Monday")
pp.pprint(cal.get_day("Monday"))
print("Tuesday")
pp.pprint(cal.get_day("Tuesday"))
print("Wednesday")
pp.pprint(cal.get_day("Wednesday"))
print("Thursday")
pp.pprint(cal.get_day("Thursday"))