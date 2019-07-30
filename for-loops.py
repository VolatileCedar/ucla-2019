import random
a = [5,6,7,8,random.randint(0,20)]
b = []
for x in a:
    print(x)
    b.append(x*2)
print(a)
print(b)

a = []
for i in range(10):
    #GENERATE A RANDOM NUMBER AND APPEND IT TO A