print("hello")
def cal():
    x = int(input("enter a number"))
    y = input("enter a symol from the *,/+,-")
    z = int(input("enter a number"))
    if y == "*":
        print(x*z)
    if y == "/":
        print(x/z)
    if y == "+":
        print(x+z)
    if y == "-":
        print(x-z)
cal()
while True == True:
    a = input("do you want to calculate again?, yes or no").lower()
    if a == "yes":
        cal()
    else:
        break