# Create a lambda function that multiplies argument x with argument y

m = lambda x, y: x*y
print(m(3,5))

# Write a Python program to create Fibonacci series to n using Lambda

from functools import reduce
 
fibo = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])

print("Fibonacci series upto 10:")
print(fibo(10))

# Write a Python program that multiply each number of given list with a given number 

num_list = [1,2,3,4,5]
n = 3
print()
print("List before multiplication ", num_list)
print("Given number ", n)
final_number=list(map(lambda number:number*n,num_list))
print("List after multiplication")
print(' '.join(map(str,final_number)))

# Write a Python program to find numbers divisible by 9 from a list of numbers 

number_list = [12, 18 ,24,27 ,35,45]
res = list(filter(lambda x: (x % 9 == 0), number_list))
print("Numbers that are divisible by 9 ",res)

# Write a Python program to count the even numbers in a given list of integers 

list1 = [12,25,83,92,56,18,35] 

even_count = len(list(filter(lambda x: (x%2 == 0) , list1))) 
  
print("Even numbers in the list: ", even_count)
