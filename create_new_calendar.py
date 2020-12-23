# Created by Warren Fletcher (wfletch)

import sys, getopt
import json
import cal_functions as cf

# What Days of the week do we want to have in our calander
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]

def get_next_day(current_day):
	"""
	Given the current day, we return the next day afterwords
	We do this by searching for the index in the list(days_of_week) of the current_day supplied
	We then icrament that index by 1 to get the next day
	we then query the list with the new index and return that array


	Edge Case: If we are on Sunday (Index = 6). We return Index 0 (Day = Monday)
	"""
	current_day_index = days_of_week.index(current_day)
	if current_day_index ==  len(days_of_week) -1 : #Get Length of the array (7). -1 because we are using and index
		current_day_index = 0
	else:
		current_day_index +=1
	return days_of_week[current_day_index]

if __name__ == "__main__": 
	# This is a special 'magic' function. It essentially runs this code if the code is ran from the command line
	# __name__ == __main__ means ran from command line. Don't worry about this!
	user = input("Enter Name of user to create:\t\t") #User name is used to save output.
	first_day_of_year = input("Enter first day of the year (01/01/21):\t")

	# Check to make sure the user supplied date is a valid one.
	if first_day_of_year not in days_of_week:
		print("Invalid Start Day")
		print(', '.join(days_of_week) + " are valid days")
		sys.exit(-1)


	# There are only 365 days in the year (366 if leap year). We use this to keep track of the number of days
	number_of_days = 365
	# Start on day 1 (01/01/xxxx)
	current_day_number = 1
	# Week starts on 0 (The first week of the year is DEFINED as starting on a monday)
	# Therefore if it starts on a Wednesday, those days are technically part of the last week of the previous
	# Year
	current_week = 0

	cal = {} #This is the dictionary of the calander
	current_day = first_day_of_year

	# Run this while loop UNTIL the number of days we have inputted has reached 0
	while current_day_number < number_of_days:
		if current_day == 'Monday': #New weeks start on Monday
			current_week += 1
		if current_week not in cal: #If the dictionary does not have the current week yet. Set it to be empty
			cal[current_week] = {}
		cal[current_week][current_day] = {} # This creates an empty day entry. This is a 'nested' Hash
		# cal[current_week][current_day] = cf.get_time_intervals() #<--- TODO:SEE WHAT THIS DOES??!
		current_day_number+=1 #Increment the number days
		current_day = get_next_day(current_day) #Get the next day of the week For next iteration.

	# This just saves the contents of the cal dictionary to '.json' file
	with open(user + '.json', 'w') as fp:
		json.dump(cal, fp)
		print("Output Saved As: " + user + '.json')