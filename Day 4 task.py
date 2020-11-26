#1.Write a program to create a list of n integer values and do the following
#Add an item into the list(using function)
l = [10,20,30,40,50]
l.append(60)
print(l)
#Delete(using function)
l1 = [20,'abc',40,'def',60]
l1.remove('abc')
print(l1)
#Store the largest number from the list to a variable
l2 = [56,6,31,20,87]
print("Largest number is:",max(l2))
#Store the smallest number from the list to a variable
l3 = [56,6,31,20,87]
print("Smallest number is:",min(l3))
#2.Create a tuple and print the reverse of the created tuple
a = ("Python")
b = reversed(a)
print(tuple(b))
#3.Create a tuple and convert tuple into list
t = ('abc',631,'Name')
l = list(t)
print(type(l))
print(l)

