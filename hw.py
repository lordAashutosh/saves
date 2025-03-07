# # Original list of numbers
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Create a new list with only the even numbers
# newlist = [n for n in num if n % 2 == 0]

# # Output the new list
# print("New list with even numbers:", newlist)




# matix 
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# count=0
# for i in matrix:
#     for j in i: 
#         count+=j
# print(count)


# name=input("which value to be appended??")

# if name in fruits:
#     print(f"{name} already exists")
#     print(fruits)

# else:
#     fruits.append(name)
#     print(f"{name} is appended to the list of fruits")
#     print(fruits)


# # find which digit has duplicatwe record....
# lst1 = [1,2,2,3,3,1,4,5,6,7,8,7,9,9]
# test_lst1=lst1
# lst1_set=set(lst1)
# print(lst1_set)

thislist=['banana',"range",'kiwi',"cherry"]
thislist.sort()
print(thislist)


thislist=['banana',"Orange",'kiwi',"cherry"]
thislist.sort(key = str.lower)
print(thislist)
