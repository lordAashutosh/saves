# x = 1
# y = 2
# def addition(x,y): #function defination
#    """ add two number and print ther sum"""#doc_string, documentation string
# sum = x+y
#     print(sum)
#     print(addition(1,2))
# from math import sqrt
# x=1
# y=2
# def addition(x,y):
#      sum = x + y
#      return sum
# Step 1: Define the function
def add_numbers(a, b):
    return a + b  # Return the sum of the two numbers

# Step 2: Call the function with desired arguments
result = add_numbers(10, 20)

# Step 3: Print the result
print("The sum is:", result)

def addition(x,y=0):
    sum = x+y
    return sum
results = addition(10)
print("the sum is:",results)

def calculator(x,y):
    add = x+y
    sub = x-y
    mul = x*y
    div = x/y
    return add,sub,mul,div
    # return sub
    # return mul
    # return div
x = calculator(10,23)
print("the result is:",x)
# def additione(*args):
#     print(agrs)
# y = additione(2,5)
# print("the no is :",y)
def additionss(*args):
    sum = 0
    for i in args:
        sum +=1

    return sum
    a = additionss(2,5,6,56,14)
    print(f"the result is {a}")