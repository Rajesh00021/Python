# Python return statement 
# A return statement is overall used to invoke a function so that the passed statements can be executed

# Example 1
def fun(x,y):
  return (x+y)

res = fun(10,20)
print("Result: {}".format(res))

# Example 2
def greet(name):
    return "Hello " + name # function returns a value does not print it
greeting = greet("Rajesh")  # storing return value in greeting variable and printing it
print(greeting)

# Printing means showing a value in the console.
# Returning means giving back a value from a function.
