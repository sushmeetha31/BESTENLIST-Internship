#DAY 9 TASK
#1)Create a lambda function that multiplies arguement x with arguement y

c = lambda x, y : x * y
print(c(4,3))

#2)Write a Python program to create Fibonacci series to n using Lambda

from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
print(fib(6))

#3)Write a Python program that multiply each number of given list with a given number

nums = [3, 4, 6, 9 , 12]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

#4)Write a Python program to find numbers divisible by 9 from a list of numbers

n = [18, 45, 63, 33, 81, 220]
result = list(filter(lambda x: (x % 9 == 0), n))
print("Numbers divisible by 9 are",result)

#5)Write a Python program to count the even numbers in a given list of intergers 

list1 = [20, 27, 4, 46, 67, 99, 38]  
even_count = len(list(filter(lambda x: (x%2 == 0) , list1))) 
print("Even numbers in the list: ", even_count) 

