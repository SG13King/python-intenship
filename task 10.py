# 1. Write a Python program for all the cases which can check a string contains only a certain set
# of characters (in this case a-z, A-Z and 0-9)
import re

str=input("Enter the string : ")
str=str.replace(" ","")
x= re.search("\W",str)
if x:
    print("Wrong match....Your string contains special characters..Enter only alphabets and numbers")
else:
    print("Perfect string !!!!!!")

# 2. Write a Python program that matches a word containing 'ab'

import re

str=input("Enter the string : ")
x = re.search("ab", str)
if x:
    print("Yes , there is word which match 'ab' in the given string")
else:
    print("There is no word matches with the given string containing 'ab'")


# 3. Write a Python program to check for a number at the end of a word/sentence
 
import re

string=input("Enter the string : ")
x=re.search("\d$",string)
if x:
    print("THERE IS A NUMBER AT THE END OF THE WORD/SENTENCE")
else:
    print("THERE IS NO NUMBER PRESENT AT THE END OF THE WORD/SENTENCE")

# 4. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
import re

str=input("Enter the string or word:")
if(re.search("\d",str)):
    print(str)
    x=re.finditer(r"([0-9]{1,3})",str)
    print("The numbers of length between 1 to 3 in the given string:")
    for i in x:
        print(i.group())
else:
    print("Enter a string with some values of numbers..")

    
# 5. Write a Python program to match a string that contains only uppercase letters
import re

x=input("Enter the string/word :")
y=re.findall("[A-Z]",x)
if y:
    print("There is a perfect match....")
else:
    print("Not a perfect match......")
