import time
a = int(input("enter a number of seconds"))
for i in range(a):
    a = a-1
    print(a)
    if a == 0:
        break