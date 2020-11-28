#DAY 6 TASK
#1)Write a program to loop through a list of numbers and add +2 to every value to elemenys in list

n = [1,2,3,4,5,6,7]
for i in n:
    i += 2
    print(i)

'''2)Write a program to get the below pattern
54321
4321
321
21
1'''

rows = int(input("Enter the number of rows: "))  
for i in range(0, rows + 1): 
    for j in range(rows - i, 0, -1):  
        print(j, end=' ')  
    print()
    
#3)Python program to print the Fibonacci series

n = int(input("\nPlease Enter the Range Number: "))
f1 = 0
f2 = 1
for Num in range(0, n):
           if(Num <= 1):
                      f0 = Num
           else:
                      f0 = f1 + f2
                      f1 = f2
                      f2 = f0
           print(f0)
    

#4)Explain Armstrong number and write a code with a function 

n = int(input("Enter a number: "))
sum = 0
temp = n
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")

#5)Write a program to print the multiplication table of 9

n = int(input("Enter the multiplication number: "))
r = int(input("Enter the range:"))
print("Multiplication table of",n)
for i in range(1,r+1):
    print(i,'x',n,'=',i*n)

#6)Check if a program is negative or positive

n=int(input ("Enter your number:"))
if(n>0):
  print("Number is positive.")
else:
  print("Number is negative.")

#7)Write a program to convert the number of days to ages

Days=int(input ("Enter Days:"))
Ages=(int)(Days//365)
print("Days to Ages:", Ages)

#8)Solve Trigonometry problem using math function write a program to solve using math function

import math 
x = math.pi/5
y = 4
z = 5
print ("The value of tangent of pi/5 is : ", end="") 
print (math.tan(x))  
print ("The value of hypotenuse of 4 and 5 is : ", end="") 
print (math.hypot(y,z)) 

#9)Create a calculator only on a code level by using if condition(Basic arithmetic calculation)

print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")


ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")
