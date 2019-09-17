#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  #f = open("textfile.txt", "w+")

  # Open the file for appending text to the end
  #f = open("textfile.txt", "a")
  f = open("textfile.txt", "r")

  if f.mode == 'w':
    # write some lines of data to the file
    for i in range(10):
      f.write("This is line #" +str(i) + "\r\n")
  
  if f.mode == 'a':
    # write some lines of data to the file
    for i in range(5):
      f.write("This is line #" +str(10+i) + "\r\n")

  # close the file when done
  
  # Open the file back up and read the contents
  if f.mode == 'r':
    print(f.mode)  
    #contents = f.read()
    #print(contents)

    fl = f.readlines()
    for x in fl:
      print(x)

  f.close()
  
if __name__ == "__main__":
  main()
