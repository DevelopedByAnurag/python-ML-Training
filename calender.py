# Other modules to play with (look them up in the "Python documentation" on the Python website! Google for it.)
#import datetime
#import time

# Import the Calendar module so we can use it
import calendar

# Give us the week headers, each 3 letters long
print(calendar.weekheader(3))
print() # these empty prints are just for spacing. they print a blank space

# Give us the integer value of what the first weekday is (Monday is 0, TUesday is 1, etc...)
print(calendar.firstweekday())
print()

# Print out the specified month
print(calendar.month(2019, 3))
print()

# Get the specified month in array form (if you don't understand the distinction, it's okay.)
print(calendar.monthcalendar(2019, 3))
print()

# Print out the specified year
print(calendar.calendar(2019))
print()

# Find out what day of the week (Mon is 0, Tue is 1, Wed is 2, etc...) the specified day is
day_of_the_week = calendar.weekday(3000, 3, 8)

# Tell us if the specified year is a leap year
is_leap = calendar.isleap(2020)
print(is_leap)
print()

# Specify how many leap days there are in the specified range of years (exclusive)
how_many_leap_days = calendar.leapdays(2000,2004)
print(how_many_leap_days)



