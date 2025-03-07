name123="###############hello###world#############"
lside_lenght = len(name123) - len(name123.lstrip('#'))
rside_lenght = len(name123) - len(name123('#'))
name1 = name123.strip("#")
name_lst = name1.split("###")
total = '#' * lside_lenght + "###".join(name_lst) + "#"rside_lenght
print(total) 

s = "HELLO"
# print(s.isupper())
# a = "hello"
# print(s.islower())
# sc= "hello, {}!"
# print(sc.format("python"))

a=5
b=10
s=f"the sum of {a} and {b} is {a+b}"
print(s)

# escape charcter
# txt = "we are the so-called \"viking\"from the north"
# print(txt)

#creating the list
number=[1,2,3,4,5]

#creating a list of string
fruits=['applr','banana','cherr']
mixed_list = [10,'hello', True]

#slicing list
print(number[1:4])
print(fruits[:2])
print(mixed_list[2:])   

#changing element
fruits=["apple","cherry"]
# fruits[1] = "mango"
# print(fruits)
# fruits[1] = "orange"
# print(fruits)
#    #adding  element
# fruits.append('banana')
# print(fruits)

# #removing elements
# fruits.remove("orange")
# print(fruits)
# for a in fruits:
#     if fruits == "cherry":
#         print("index od cherryy is",a)

fruits = ['apple','banana','cherry','pineapple']
for x in range(len(fruits)):
    if fruits[x] == 'cherry':
        print('index',x)
        fruits[x] = "mango"
        fruits[x] = input('enter the nmae of friu')



print(fruits)

    # DAY 6 WAS FUVKING BORING , BORING ..........
    