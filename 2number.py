import random
x = random.randint(1, 100)
y = random.randint(1, 100)
res = (x*y)
c = 0
while True:
    a = int(input("Enter a number"))
    if a == res:
        print("Congratulations")
        c = c+1
        print("You got it in", c, "tries")
        break
    if a != res:
        c = c+1
        print("try again")
        if a > res:
            print("Higher")
        if a < res:
            print("lower")
    if c == 3:
        print("you lose")
        break

