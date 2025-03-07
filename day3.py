#day 3 of  learning python
numbers= [1,2,3,4,5]
for num in numbers:
    print("num")
number=[1,2,3,4,5]
for num in number:
    if num%2!=0:
        print(num)
else:
     pass
#for calculating n  in the banana
x=0
for a in "banana":
    if a=="n":
        x = x + 1

print("the no of n in banana is",x)      
fruit = ["apple","banana","cherry"]
for x in fruit:
    print(x)
    if x=="banana":
        break

for a in "banana":
    print(a)
    if a=="n":
        break
fruit = ["apple","banana","cherry"]
for x in fruit:
    if x == "banana":
        continue
    print(x)
#skip 5 and break 7
num = [ 1,2,3,4,5,6,7,8,9,10]
for x in num:
    if x == 5:
       continue
    elif x == 7:
        break
    print(x)
a=1
for x in range(6):
    if x == 0:
        continue
    a = a * x

print(a)
#variable define is necessary
for x in range(0,31,2):
    print(x)
for x in range(1,30,2):
    print(x)
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

# to make  a  set
set1 = [1,2,3,4,5,6,7]
set2 = ["a","b","c","d","e","f"]

for x in set1:
    for y in set2:
        print(x,y)