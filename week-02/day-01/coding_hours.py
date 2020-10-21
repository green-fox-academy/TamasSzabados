# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

daily_hours = 6
semester_weeks = 17
workdays = 5
weekly_hours = 52

print(str(daily_hours * semester_weeks * workdays) + " hours")

percentage_hours = str(daily_hours*workdays/weekly_hours*100)

print(percentage_hours[:5] + " %")
