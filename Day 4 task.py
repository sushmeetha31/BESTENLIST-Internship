#1.Write a program to create a list of n integer values and do the following
#Add an item into the list(using function)
#Delete(using function)
#Store the largest number from the list to a variable
#Store the smallest number from the list to a variable
l = [10,20,30,40,50]
l.append(60)
print(l)
l.remove(20)
print(l)
print("Largest number is:",max(l))
print("Smallest number is:",min(l))

#2.Create a tuple and print the reverse of the created tuple
a = ("Python")
b = reversed(a)
print(tuple(b))

#3.Create a tuple and convert tuple into list
t = ('abc',631,'Name')
l = list(t)
print(type(l))
print(l)

