def myFun(num):
    num[0] = 20


list = [1, 2, 3, 4, 5]
myFun(list)
print(list)


def my_function():
    print("Hello from a function")
    print("Day 5 - Functions")


my_function()

# Exercise 1


def arith_func(p, q):
    print("Addition of two numbers is: ", p+q)
    print("Subtraction of two numbers is: ", p-q)
    print("Multiplication of two numbers is: ", p*q)
    print("Division of two numbers is: ", p/q)


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

arith_func(a, b)

# Exercise 2


def covid(name, temp):
    if not temp:
        temp = 98
    n = name
    t = temp
    print("Name: ", n)
    print("Temperature: ", t)


x = input("Enter name: ")
y = input("Enter temperature: ")
covid(x, y)
