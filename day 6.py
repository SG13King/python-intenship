# Write a program to loop through a list of numbers
# and add +2 to every value to elements in list
import math
a = [1, 2, 3, 4, 5]
print(a)
n = 0
for n in range(0, len(a)):
    a[n] = a[n]+2

print(a)

# Write a program to get the below pattern
# 54321
# 4321
# 321
# 21
# 1

print()
n = 5
for i in range(n, 0, -1):
    j = i
    while j > 0:
        print(j, end=" ")
        j = j-1
    print()

# Python Program to Print the Fibonacci sequence

nterms = int(input("Enter number of terms: "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# Explain Armstrong number and write a code with a function

# 153 = (1^3)+(5^3)+(3^3)
# if this is equal to 153 then it is a Armstrong


def armornot(num):
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


n = int(input("Enter a number to check armstrong or not: "))
armornot(n)

# Write a program to print the multiplication table of 9


def mul_table():
    n = 9
    for i in range(0, 11):
        print(i, " * ", 9, " = ", i*9)


print()
print("Multiplication table of 9")
mul_table()

# Check if a program is negative or positive


def pos_or_neg(n):
    if n >= 0:
        print("Positive")
    if n < 0:
        print("Negative")


print()
c = int(input("Enter a number: "))
pos_or_neg(c)

# Write a program to convert the number of days to ages

print()
weekdays = 7


def find(number_of_days):
    year = int(number_of_days / 365)
    week = int((number_of_days % 365) /
               weekdays)
    days = (number_of_days % 365) % weekdays

    print("years = ", year,
          "\nweeks = ", week,
          "\ndays = ", days)


nod = int(input("Enter number of days: "))
find(nod)

# Solve Trigonometry problem using math function
# write a program to solve using math function

print()
print("Trigonometry problem using math function")
print(math.sin(60))
print(math.tan(45))
print(math.cos(60))

# Create a calculator only on a code level by using if condition

print()


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")