import sys, getopt
import json


days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]

def get_next_day(current_day):
	current_day_index = days_of_week.index(current_day)
	if current_day_index ==  len(days_of_week) -1 :
		current_day_index = 0
	else:
		current_day_index +=1
	return days_of_week[current_day_index]

if __name__ == "__main__":
	user = raw_input("Enter Name of user to create:\t\t")
	first_day_of_year = raw_input("Enter first day of the year (01/01/21):\t")
	if first_day_of_year not in days_of_week:
		print("Invalid Start Day")
		print(', '.join(days_of_week) + " are valid days")
		sys.exit(-1)

	number_of_days = 365
	current_day_number = 1
	current_week = 0

	cal = {}
	current_day = first_day_of_year
	while current_day_number < number_of_days:
		if current_day == 'Monday':
			current_week += 1
		if current_week not in cal:
			cal[current_week] = {}
		cal[current_week][current_day] = {}
		current_day_number+=1
		current_day = get_next_day(current_day)


	with open(user + '.json', 'w') as fp:
		json.dump(cal, fp)
		print("Output Saved As: " + user + '.json')