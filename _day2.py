#day 2 of learning python

# Taking a value form a user:

num1 = input("enter your name : ")

#taking integer input
num2 = int(input("enter a integer number : "))
num3 = int(input("enter a integer number : ")) 

# Having sum
a = num2 + num3
print("sum is",a)

# type  validation  
value =  input("enter a number: ")
if value.isdigit():
    num4 = int(value)
    print(f"converted to the integer : {num4}") 
elif '.'in value:
    num4 = float(value)
    print(f"converted to the float: {num4}")
else:
    print("invalid number")


    # Number type of conditionals
x = 10
a = 5
if x > 5:
    print(f"{x} is grater than 5")
if a<=15:
    print(f"{x} is smaler than 15")


#between no
x=7
if x > 5 and x > 10:
    print(f"the {x} lies between  them")
else:
    print(f"{x} does not lies between them") 

# Its for the condition 
num = input("enter a fruits")
if num =="apple" or num == "orange":
    print(f"{num} is either apple or orange")
else:
    print(f"the num is {num}")


    
num = int(input("enter a integer: "))
if num != 5:
     print("no is not 5 ")
else:
     print("no is 5")
#nested conditionals
x=5
if x > 0:
     if x < 10:
         print("x is positive single digit")
     else:
         print("x is positive doule digit")
elif x == 0:
    print("x is zero")
else:
     print("x is negative")
a=2
b=330
print(a) if a > b else print(b)
a=2000
b=330000
sum = 1 if a > b else 2
print(sum)
a=100
b=299
if a > b:
     print("A")
else:
     if a == b:
         print("=")
     else:
         print("B")
#shortcut of if else
print("A") if a > b else print("=") if a == b else  print("B")
if not a > b:
    print(" a  is not greater than b")
if b > a:
    pass