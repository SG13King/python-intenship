#Write a program using zip() function and 
#list() function, create a
#merged list of tuples from the two lists given.

def merge(list1, list2): 

    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 

list1 = [1, 2, 3] 
list2 = ['Siva', 'SG', 'Sivaganesh'] 
print(merge(list1, list2))

#First create a range from 1 to 8. Then using zip, 
#merge the given list
#and the range together to create a new list of tuples.

list_1=["Siva","SG","Virat","Ganesh","Kumar","Selena","kapoor","Rakul"]

range=list(range(1,8))
lst=list(zip(list_1, range))
print(lst)

#Using sorted() function, sort the list in ascending order.

list=[11,84,114,111,105,78,106]

list.sort()
print("Sorted List is " , list)

#Write a program using filter function, 
#filter the even numbers so that
#only odd numbers are passed to the new list.

numbers = [11,10,78,14,54,18,45,98,55,68,71]
def Odd_numbers(num):
    if(num%2 != 0):
        return True
    else:
        return False

OddNums = filter(Odd_numbers, numbers)
print('Odd Numbers are:')
for num in OddNums:
    print(num)