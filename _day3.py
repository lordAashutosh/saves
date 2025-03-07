# day 3 of learning python
number = [1,2,3,4,5]   # to print the list
for num in number:
    print(num)
 #to print odd number...
for num in number:
        if num %2 != 0:
            print(num)   # odd number in the list 
        else:
            pass


#for calculating n the banana
x=0
for a in "banana":
     if a=="n":
          x = x+1

print(f"the no of n in banana is {x}")