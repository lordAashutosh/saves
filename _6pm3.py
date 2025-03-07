def hello():
    xyz=8   # inside function ==> function ==> local scope
    print(xyz)
hello()
name = 'ram' #global scope
print(name)
# print(xyz)   # since xyz variablr is inside the function so error occur
def hi():
    print(name)
hi()

x= 5
# def hello():
#     print(y)  # local scope ==> global scope ==> built in ==> error
# hello(y) # since y is in no where so it give error.

a = sorted([1,2,32,78,12,0])
print(a)
def hello():
    x = 2 
    print(x) # local scope ==> 2

print(x) # global scope==> 5
hello()
print(x) # global scope ==> 5



# def hello():
#     x = x + 2 
#     print(x) # local scope ma navayera error aako

# print(x)
# hello()
# print(x) 
x = 5
def hello():
    y = x + 2  # local scope ==> global scope==>5
    print(y)

print(x)
hello()
print(x)



def helllo():
    global x
    x = x + 2
    print(x)

print(x) # global ==> 5 + 2 ==> 7
hello()
print(x)# global ==> 7 


# factorial 
def factorial(n):
    fact = 1
    for i in range(n,1,-1):
        fact *= 1
    return fact
    
result = factorial(5)
print(f"factorial of 5 is {result}")


# list(range(5,0,-1))# start,stop,step



# def hihello():
#     print("hello")
#     hihello() # recursion ==> calling itself

# hihello()

# recursive
# 1. calling itself
# 2. base condition ==> terminating condition / returning 




def factorials(n):
    if n <= 1:
        return 1
    else:
        return n * factorials(n-1)
    # formula = factorial(n) = factorial(n) * factorial(n-1)
print(factorials(5))


# def fact(n):
#     if n < 0:
def square(n):
    return n ** 2
print(square(5))

# squre = lamda n; n ** 2 # anonymous function / lamda function


def sum(x,y):
    # x = input("enter a integer",x)
    # y = input("enter a integer",y)
    sum_of_them = x + y 
    print(sum_of_them)

sum(2,4)


# def addition(x,y):
#     return x + y
# additon(4,6) 
#0, 0.0,0j,'', Nonw.{},[],set(), false,range(0)==> boolean value / truthnes is false
bool('0')
print(bool('0'))
print(any([0,'',(),{},set(),False,-1]))
# print(all[1,True,'hello'])
# print(all[0,'',None,[],{},set(),False])
# help(filter)
a=list([1,2,0,False,5,'ram',{},5.5])
print(a)


def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False
    
print(is_odd(7))


def is_oddd(n):
    return n % 2 ==1
print(is_oddd(4))


is_odd = lambda n: n % 2 == 1
print(is_odd)


square = lambda n: n**2 # ananymous function / lamda function
print(square(6))




print(any([0,'',None,[],{},set(),False,-1])) # aauta pani true xa  vani true aauxa 
print(all([0,'',None,[],{},set(),False,-1])) # kunai aauta pani false xa  vani false aauxa
# help(filter)
# a = list(filter(None,[1,2,0,False,5,'ram',{},5.5]))
# print(a)


def check_number(n):
    if n % 2 == 1:
        return True
    else:
        return False
    
print(check_number(8))


# same as above but in short order
def is_odd(n):
    return n % 2 == 1
print(is_odd(9))
    
odd_no = lambda n:n%2==1
print(odd_no(9))

