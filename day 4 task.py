# Write a program to create a list of n integer values and do the following
# Add an item in to the list (using function)
n = int(input("Enter number of integer values: "))
a = [0]
for i in range(1, n):
    a.append(i)
print(a)

# Delete (using function)
a.remove(2)
print("After removing 2")
print(a)

# Store the largest number from the list to a variable
print("Largest number from the list")
b = max(a)
print(b)

# Store the Smallest number from the list to a variable
print("Smallest number from the list")
b = min(a)
print(b)

# 2) Create a tuple and print the reverse of the created tuple
print("Reverse of created tuple")
t = (1, 2, 3, 4, 5)
b = reversed(t)
print(tuple(b))

# 3) Create a tuple and convert tuple into list
print("Tuple into list")
t = (1, 2, 3, 4, 5)
b = list(t)
print(b)