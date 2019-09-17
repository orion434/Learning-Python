#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print (timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
today = date.today()
print("Today is ", str(now)+"(" + str(today) + ")\n" )

# print today's date one year from now
print("One year from now, it will be: " + str(now+timedelta(days=365)))
print("One year from now, it will be: " + str(today+timedelta(days=365)) + "\n")

# create a timedelta that uses more than one argument
print("+2d,3w: " + str(now+ timedelta(days=2, weeks=2)) )
print("+2d,3w: " + str(today+ timedelta(days=2, weeks=2)) + "\n")

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
print("One week ago it was: " + t.strftime("%A %d %B, %Y")  + "\n")

### How many days until April Fools' Day?
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
  print("April Fool's day already went by %d days ago" % ((today-afd).days) )
  afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd-today
print ("It's just", time_to_afd.days, "days until next April Fools' Day!")

