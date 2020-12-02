#DAY 10 TASK
#1)Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z,A-Z and 0-9)

import re
def s(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(s("*&%@#!}{"))
print(s("32AsdEafr4"))

#2)Write a Python program that matches a word containing 'ab'

import re
def mat(text):
        patterns = '\w*ab\w*'
        if re.search(patterns,  text):
                return ('Matched')
        else:
                return('Not matched')

print(mat("ab"))
print(mat("basic"))
print(mat("abnormal"))

#3)Write a Python program to check for a number at the end of a word/sentence

import re
a = "Daily Tasks"
print ("The original string is : " + a)
result = len(re.findall(r'\w+', a))
print ("The number of words in string are : " + str(result))

#4)Write Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

import re
result = re.finditer(r"([0-9]{1,3})", "number 1, 12, 16, and 631 are present")
print("Number of length 1 to 3")
for n in result:
     print(n.group(0))
	 
#5)Write a Python program to match a string that contains only uppercase letters

import re
def upp(text):
        patterns = '^[A-Z0-9]*$'
        if re.search(patterns,  text):
                return ('Matched')
        else:
                return('Not matched')

print(upp("UPPERCASE"))
print(upp("lowercase"))
     
