i = 0
while i<=10:
    print(i)
    i =i+1

i = 1
factorial = 0
while i < a+1:
    factorial = factorial * i
    i =i+1
    print("a-factorial")

a = int(input())
f0 = 0
f1 = 1
next_val = f0+f1
i = 0
while i<=a:
    next_val = f0+f1
    f0 = f1
    f1 = next_val
print(next_val)
