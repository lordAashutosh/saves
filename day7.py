# # Initial string with hashes
# name = "##############Hello###world#############"

# #  Remove all '#' characters and add a space between "hello" and "world"
# cleaned_name = name.replace("#", "")                                                        #.replace("Hello", "hello").replace("world", "world")

# # Print the cleaned result (hello world)
# print("Cleaned Name:", cleaned_name)
# cleaned_name1 = cleaned_name[0:5] + " " + cleaned_name[5:11]
# print("Cleaned Name:", cleaned_name1)
# # : Reconstruct the original pattern with hashes
# reconstructed_name = name.replace("Hello", "hello").replace("world", "world")

# # : Print the reconstructed name
# print("Reconstructed Name:", reconstructed_name)

 

      # creating the list of lits
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
for x in matrix:
    print(x)
    print(type(x))
    print(x[0])
    break

print(matrix[0][1])

#ITERATING THROUGH A LIST OF LISTS

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()


    # list- mutable
    #tuple - immutable

    fruits = ['apple','banana','cherry']
    fruits.insert(1,'orange')
    print(fruits)

    thislist = ["apple","banana",'cherry']
    tropical = ["mango","pineapple","papaya"]
    thislist.extend(tropical)
    print(thislist)


    #add tuple in a list
      # ADD ANY ITERABLE
thislist = ["apple",'banana',"cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)


# to remove
thislist.remove('banana')
print(thislist)
thislist.pop(1)
print(thislist)

# del keyword
del thislist[0]
print(thislist)
# clear keyword
tropical.clear()
print(tropical)


# sort
thislist=["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)
# for decending order
thislist.sort(reverse=True)
print(thislist)
thislist.sort(key = str.lower)
print(thislist)

thislist.reverse()
print(thislist)

mylist = thislist.copy()#deeep copy
thislist.append("mango")
print(mylist)

mylist1 =thislist #shallow copy

list1=["a","b","c"]
list2=[1,2.3]
list3 = list1 + list2
print(list3)
list1.extend(list2)


# list comprehension
fruits = ["apple","banana","cherry","kiwi",'mango']
newlist = []
for x in fruits:
     if "a" in x:
      newlist.append(x)
print(newlist)      



newlist = [x for x in fruits if "a" in x]
print(newlist)



a=["b",'c','d','g','h']
x = sorted(a)
print(x)