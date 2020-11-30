#1
filename = 'exception_data.txt'
print("First Example : Files")
try:
    with open(filename) as fin:
        for line in fin:
            items = line.split(',')
            total = 0
            try:
                for item in items:
                    num = int(item)
                    total += num
                print('Total = ' + str(total))

            except:
                print('Error converting to integer. ', items)
except:
    print('Error opening file. ' + filename)

finally:
    print('This is our optional finally
          block. Code here will execute no matter what.')

print("-------------------------
      -------------------------------
      ------------------------------")
print("Second Example : ")
# Second example: name Error type in except block;
#  call function from try block.


def this_fails():
    x = 1/0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


def divide_me(n):
    x = 1/n


i = int(input('enter a number '))
try:
    divide_me(i)
except Exception as e:
    print(e)  # this will print the
    # error msg but don't kill the execution of program
else:
    # this will execute if divide_me(i) run sucessfully without an error
    print('Your Code Run Successfully')
finally:
    print('thanks')  # this will execute in every condition
print("---------------------------
      ------------------------------------------
      ----------------")

#2
import math
while 1:
    print("1) Add")
    print("2) Subtract")
    print("3) Divide")
    print("4) Multiply")
    print("0) Exit")

    try:  # This is a try statement used to handle errors
        answer = int(input("Option: "))
        if answer == 1:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first + second
            print("Answer:", float(final))
            print()
        elif answer == 2:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first - second
            print("Answer:", float(final))
            print()
        elif answer == 3:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first / second
            print("Answer:", float(final))
            print()
        elif answer == 4:
            first = float(input("First Number: "))
            second = float(input("Second Number: "))
            final = first * second
            print("Answer:", float(final))
            print()
        elif answer == 0:
            break
        else:
            print("\nPlease select a valid option number\n")
    except NameError:

        print("\nNameError: Please Use Numbers Only\n")

    except SyntaxError:

        print("\nSyntaxError: Please Use Numbers Only\n")

    except TypeError:

        print("\nTypeError: Please Use Numbers Only\n")

    except AttributeError:

        print("\nAttributeError: Please Use Numbers Only\n")
#3
try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print(num1+num2)
except NameError:
    print("\nNameError: Please Use Numbers Only\n")

#4
we use try - except in checking and validation
apart from checking and validation 
try-except is not required

#5
try:
    n = input("Please enter an integer: ")
    n = int(n)
    print("Great, you successfully entered an integer!")
except ValueError:
    print("Not a valid integer")
