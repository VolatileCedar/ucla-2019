import random
a = []
sum = 0
for x in range(0,10):
    a.append(random.randint(0,100))
    sum += a[0]
print(a)
print(sum)