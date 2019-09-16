# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)

# # re-declaring the variable works
f = "abc"
print(f)

# # ERROR: variables of different types cannot be combined
#print("String + number gives an error" + 123)
print("String + string is ok: " + "123")

# Global vs. local variables in functions
def someFunction():
    f = "scope inside the function"
    print(f)

def globalFunction():
    global f
    f = "global f"
    print(f)


someFunction()
print(f)

globalFunction()
print(f)

#del(f)
#print(f)
