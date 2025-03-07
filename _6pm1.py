students = {'Alan','bill','ramesh','corry','ram'}
output = {}
for student in students:
    output[student] = len(student)

print(output)

output = {}
for student in students:
    output.update({student: len(student)})
print(output)

list(range(0,10,2))

student = ['alan','bill','ramesh','corry','ram']
for i in range(0,10,2):
    print(i)


students = ['alan','bill','ramesh','corry','ram']
# 0 = alan
# 1 = bill
# 2 = ramesh and so on ....on indexing


i = 0 
for student in students:
    print(f"{i}= {student}")
    i+=1


a = 0
for a in range(0,len(students)):
    print(f"{a} = {students[a]}")


us_price = {'milk':2.83,'bread':2.6,'butter':3.6}
# 1 usd = npr 132
# {'milk':267.96,'bread':343.2,'butter':475.2}
nep_price={}
for k, v in us_price.items():
    nep_price.update({k:v * 132 * 1.13}) # adding tax also

print(nep_price)

us_price = {'milk':2.83,'bread':2.6,'butter':3.6}





us_price = {
    'milk':2.03,
    'bread': 2.6,
    'iphone':999,
    'butter':3.6,
    'meat':5,
    'mobile':500,
    'laptop':1000,
    'television':340,
}
# print(us_price)
nep_price = {}
for k, v in us_price.items():
    if v < 5:
        nep_price.update({k:v * 132 * 1.13})
    else:
        nep_price.update({k: v * 132 * 1.20})
print(nep_price)

# pass, continue , break
age = 17
if age < 17:
    pass

print("hello")
sum=0
numbers = [1,2,6,8,9,6,10]
for i in numbers:
    if i == 6:
        pass # pass le tyo step nai run gardai na 
    else:
        sum += i

print(sum)




sum=0
numbers = [1,2,6,8,9,6,10]
for i in numbers:
    if i == 6:
        continue      #Continue le skip garxa 
    
    sum += i

print(sum)



sum=0
numbers = [1,2,6,8,9,6,10]
for i in numbers:
    if i == 6:
       break
    
    sum += i

print(sum)


names = ['ram','shyam','gita','sita']
foods = ['momo','chawein','thukpa']
for i in names:
    for j in foods:
     #   senstence = i +" " + "eats" + " " + j
     print(f"{i} eats {j}")
      #  print(senstence)


names = ['ram','shyam','gita','sita']
i = 0 # intialazier
while i < len(names): # 0 < 4 #condition
    print(names[i])
    i +=1  # incremnter / decrementer



numbers = [1,2,3,4]
i = 0 
sum = 0
while i < len(numbers):
    sum += numbers[i]
    i +=1
print(sum)


# while True::
#     print(i)         # yesle infinite no print garxa...
#     i +=1

# i = 1
# while age >= 18:
#     age = input("enter a age : ")