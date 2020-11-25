#DAY 3 TASK
#1)Write a Python script to merge two Python dictionaries
a1 = {'a':100,'b':200}
a2 = {'x':300,'y':400}
a = a1.copy()
a.update(a2)
print(a)
#2)Write a Python program to remove a key from a dictionary
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)
#3)Write a Python program to map two lists into a dictionary
keys = ['red','green','blue']
values = ['1000','2000','3000']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)
#4)Write a Python program to find the length of a set
 a = set([1,2,3,4,5)]
print(len(a))
#5)Write a Python program to remove the intersection of a 2nd set from the 1st set
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print("Original sets:")
print(s1)
print(s2)
print("Remove the intersection of a 2nd set from the 1st set using difference_update():")
s1.difference_update(s2)
print(s1)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(s1-s2)
