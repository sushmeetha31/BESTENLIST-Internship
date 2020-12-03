#DAY 11 TASK

#1)Wrie a program using zip()function and list()function ,create a merged list of tuples from the two lists given.

def merge(l1, l2): 

    merged_list = tuple(zip(l1, l2)) 
    return merged_list 
l1 = ['a', 'b', 'c'] 
l2 = [1, 2, 3 ] 
print(merge(l1, l2))

#2)First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.

l=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
r1 = list(range(1,8))
l1 = zip(l, r1)
print(l)

#3)Using sorted() function, sort the list in ascending order.

list1=[12,43,56,0.9,78,32,45,0.13,144,631]
list2=sorted(list1)
print(list2)

#4)Using filter function, filter the even numbers so that only odd numbers are passed to the new list.

list1=[85,8,56,33,45,21,45,88,90]
list2 = list(filter(lambda x: x%2 == 1, list1))
print(list2)
