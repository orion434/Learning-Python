#
# Example file for working with functions
#

# define a basic function
def func1():
    print("func 1")

# function that takes arguments
def func2(arg1, arg2):
    print("func 2")
    print(arg1, ", " , arg2)

# function that returns a value
def cube(x):
    print("func 3")
    return x**3

# function with default value for an argument
def power(num, x=1):
    print("func 4")
    result = 1
    for i in range(x):
      result = result * num
    return result

def power_v2(num, x=1):
    return num**x

#function with variable number of arguments
def multi_add(*args):
    result =0
    for x in args:
        result = result +x
    return result


func1()            # execute the function
print (func1()) # func 1 \n  None (from the print() )
#print(func1) # return an error

func2(123, 456)

cube(2)
print(cube(2))

x3 = cube(2)
print(x3)

print(power(2), "==", power_v2(2))
print(power(2,3), "==", power_v2(2,3))

print(power_v2(x=3, num=2))

print(multi_add(2,5,8,77,34))
print(multi_add(2,5,8,multi_add(18,9)))
