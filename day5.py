# its day 5 of learning python
s=""" EXTRA POINT
.....And i would like to congratulate every classmates including myself for being in this position here today. 
As Charles Dickens put it "it was the best of times and the worst of times" 
Going through the pressure of passing the tenth grade with the expectations of good GPA was stressful is how i would put it
but also really really memorable. now stepping into higher secondary level, i know that i and 
my friends will have in mind the hard work we put here in order to pass through this level,
 without regret and without remorse.

getting banned from sports in the beginning of the 10th grade, well that was 
harsh but i dont think we regret it now.

morning class was an ordeal(smiling).. waking up early in the morning and rushing to the school with runny nose 
during the winter after a bowl of oatmeal and rarely a boiled egg was difficult. 
My friend Roshan (pointing at Roshan) and I would always be disbanded during Shree Ram Sir's class... which i really did not 
understand why.. well maybe i was the only one who did not understand why."""
a=len(s)
print(a)
    #immutable data type
s = "Hello"
# s[0] = "h" 
a = s.lower()
print(a)
for i in a:
    if i == "h":
        print(i)

name="hello"
name1="world"
a = name + name1
print(a)

# string methods
# .replace
s = " hello, world!"
print(s.replace("world", "guys"))
print(s.lower())
print(s.upper())
print(s)
print(s.title())

print(s.lstrip())
print(s.rstrip())
print(s.strip())

print(s.split()) #output : ['hello', 'world']


#  joins
s=''
words=['hello', 'world','a']
print('-'.join(words))
name = "###############################hello###world#############"
name1 = name.strip('#')
print(name1)
name2 = name1.split("###")
print(name2)

nome = "###############################hello###world#############"
a=nome[0:30]
count=len(a)
name=['hello', 'world']
name1= "###".join(name)
print(name1)
name3= name1.lstrip("###############################")
print(name3)



