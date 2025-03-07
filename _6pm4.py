# def hello():
#     xyz = 8
#     print(xyz)

# hello()
# # print(xyz)  # variable insides function remains on fucntion only 
# help(map)
def square(n):
    return n ** 2
print(square(5))
print(map(square, [1,2,3,4,5,6]))
print(list(map(square, [1,2,3,4,5,6])))

print(list(map(lambda n: n ** 2 , [1,27,12,17,8])))


# lambda ma j pathayo , tei matra print hunxa 
print(list(map(lambda n: False, [1,2,3,4,5,6,7,8])))# yesma false pathako vayera ,  sabai false print vako ho
from functools import reduce
# help(reduce)

def addition(x,y):
    return x+y
print(reduce(addition, [1,2,3,4]))
# 