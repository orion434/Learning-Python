#
# Example file for working with date information
#
from datetime import date # datetime standard module in python library
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today is", today)

  # print out the date's individual components
  print(today.day, today.month, today.year)
 
  # retrieve today's weekday (0=Monday, 6=Sunday)
  days = ["M","T","W","T","F","S","S"]
  print(print(),  days[today.weekday()] )

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  now = datetime.now()
  print( now )

  # Get the current time
  #t = datetime.time(datetime.now())
  t = datetime.time(now)
  print (t)

  
if __name__ == "__main__":
  main();
  