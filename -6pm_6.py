ls = [1,2,3,4,5,6,]
#output = [ 1,4,9,16,25,36]

sqaure = []
for i in ls:
    sqaure.append(i**2)
# un pythinic way 
print(sqaure)


#list comprehension
ls = [1,2,3,4,5,6]
output = [i **2 for i in ls]
print(output)




age = 17
if age < 18:
   print("unauthorized") # pythonic way
else:
  print("authorized.")
  


#ternary operator
is_authorized = "unauthorized" if age < 18 else " Authorized"
print(is_authorized)



number = [1,23,4,3,3,2,2]
#output = ["odd", "even"]

# output = []
# for numbers in number:
#     if number % 2 == 0:
#       output.append('even')
#     else:
#       output.append('odd')
       

# print(output)






output = ['even' if number % 2 == 0 else "odd" for number in number]
print(output)



numbers = [-8,-7,3,-1,0,1,3,4,5,-7,6,8]
# output = []
# for number in number in numbers:
#    if number > 0:
#       output.append(number)
# print(output)



output = [number for number in numbers if number > 0]
print(output)



us_price = {'milk': 2.05,'bread': 2.6, "butter": 2.6}
# nep_price = {'milk': 268.6935,'bread': 268.6935, "butter": 268.6935}  


# nep_price = {}
# for k, v in us_price.items():
#     nep_price[k] = v * 132 * 1.13
# print(nep_price)
# non pythonic code here       


nep_price = {}
for k, v in us_price.items():
    nep_price.update({k: v * 135})
print(nep_price)


us_price = {'milk': 2.05,'bread': 2.6, "butter": 2.6}
nep_price = {
   k: v * 135
   for k, v in us_price.items()
}
print(nep_price)




price_us_price = {'milk': 2.05,'bread': 2.6, "butter": 2.6,'mobile':50,'televison':1000
                  ,'refigetor':700}
prices_below_5 = {product: price * 135
for product, price in price_us_price.items()
   if price < 5
   }
print(prices_below_5)
# for product, price in price_us_price.items():
#    if price < 5:
#       prices_below_5.update({product: price*135})
# print(prices_below_5)

# non pythoncnic way
# using comprehension



nep_price1= {
   product: (price * 131.07 * 1.13 if price < 5 else price*131.07)
   for product, price in price_us_price.items()

}
print(nep_price1)


