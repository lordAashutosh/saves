#this is day 4 of learning python.............
                #   while loop 
"""While loop can run infinite time.
It run and run again untill the condition is fulfill"""
# write a program to print a number upto 6 but stop print if 3 is print.
i = 0 
while i < 6:
    print(i)
    if i == 3:
        break  # to break the loop 
    i+=1

    # same program as above but skip 3.
i = 0
while i < 6:
    i +=1
    if i == 3:
        continue      #to skip 
    print(i)

#swapping 
   
x,y=1,2
x,y= y,x  # here the value of y is assign to x and value of x is assign to u 
print(x,y) #print the swapped value

#Again swapping with a temporary variable

temp=90
y=temp
x=y
print(y,x)

# swapping the value with out any temporary  variable (mathmatically)
x=10
y=20
# v=x+y  # swapping mathmatically but using 1 variable.
# y=v-y
# x=v-x
print(x,y)

# swapping mathmatically

x = x + y
y = x-y
x=x-y
print(x,y)

#strings 

name="i'm aashutosh"
print("name")
multi_line_string='''this is a multiline string
akgskasdbasbasbcka
asfasgfa'''       #phage inside the """.... """ is multi line
print(multi_line_string)


# INDEXING
   #TO PRINT THE SPECIFIC LETTR ONLY 
      #IN INDEXING FRIST LETTER IS 0 FROM LEFT RIGHT 
        #IF INDEXING FROM RIGHT SIDE IS DONE THEN COUNTING STARTS FROM -1
          # INDEXING FROM RIGHT SIDE IS CALLED NEGATIVE INDEXING
s= "hello world"
print(s[-1])
print(s[-10])
s="hello, world!"

# IN THIS 1st NO IS A STARTING POINT AND THE LAST NO IS A STOPING POINT
print(s[-6:-1])
#IF THEIR IS NO FIRST NO THEN IT WILL PRINT FROM THE START TO GIVEN END POINT
print(s[:5])
#IF THEIR IS ONLY STARTING POINT GIVEN AND ENDING POINT IS NOT GIVEN THEN IT WILL PRINT TO LAST WORD.
print(s[7:])
print(s[:12])
#            step slicing     # 
print(s[:5:3])   # IT WILL SKIP 2 DIGIT PRINT AND  SAME AGAIN
print(s[::-1])    # ITS WILL REVERSE THE  INPUT
print(s[::-2])      #  IT WILL REVERSE TEH INPUT BUT SKIP ONE DIGIT AND RUN REPEATEDLY  

#LEN IS USED TO COUNT THE NUMBER IN STRING . . . . . . . . . . . . . . 

a="hello world"
c=len(a)    # SPACE IS ALSO COUNTED .
print(c)
 
#COMBINING THE FOR LOOP , IF CONDITION , INDEXING.....

s="hello, world!"
for i in range(len(s)):
    if s[i]=="w":
        print(f'character at index {i} is {s[i]}')
    
# sting is unmuatable..it can't be change 

s="Hello, world!"
for char in s:
    if char.lower() == "h":            #sting is unmuatable so, .lower temporarly make it lower case.
        print("the character is 'h' or 'H'.")
    else:
        print(f"the character'{char}',not 'h' or 'H' ") 