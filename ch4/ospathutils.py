#
# Example file for working with os.path module
#
import os
from os import path

import datetime
from datetime import date, time, timedelta

import time


def main():
  # Print the name of the OS
  print(os.name)
  
  # Check for item existence and type
  fileName = "textfile.txt"
  print ("Item exists: " + str(path.exists( fileName )))
  print ("Item is a file: " + str(path.isfile( fileName)))
  print ("Item is a directory: " + str(path.isdir( fileName )))
  
  # Work with file paths
  filePath = path.realpath( fileName )
  print ("Item's path: " + str(filePath))
  print ("Item's path and name: " + str(path.split( filePath )))
    
  # Get the modification time

  modTime = path.getmtime(fileName)
  t = time.ctime(modTime)
  print(t)
  print (datetime.datetime.fromtimestamp( modTime  ))
  
  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp( modTime )
  print ("It has been " + str(td) + " since the file was modified")
  print ("Or, " + str(td.total_seconds()) + " seconds")
  
if __name__ == "__main__":
  main()
