s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print("Original sets:")
print(s1)
print(s2)
print("Remove the intersection")
s1.difference_update(s2)
print(s1)
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print("Original sets:")
print(s1)
print(s2)
print("Remove the intersection")
print(s1-s2)