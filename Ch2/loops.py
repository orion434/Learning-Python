#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x<2):
    print(x)
    x =x +1

  # define a for loop
  for x in range(5,7):
    print(x)

  # use a for loop over a collection
  days = ["M","T","W","T","F","S","S"]
  for d in days:
    print(d)

  print("")
  # use the break and continue statements
  for x in range(5,10):
    if (x==9): break
    if (x%2 == 0): continue
    print(x)

  print()

  #using the enumerate() function to get index 
  days = ["M","T","W","T","F","S","S"]
  for i,d in enumerate(days):
    print(i+1, " - ", d)

if __name__ == "__main__":
  main()
