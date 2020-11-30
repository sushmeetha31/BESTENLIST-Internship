#DAY 8 TASK
#1)List down all the error types and chck all the errors using a python program for all errors
#NameError
try:
    raise NameError('Picture')
except NameError:
    print("The exception demolished")

#IndexError
l = list(range(0,13))
try:
    print(L[30])
except:
    print("Error handled")
    
#ModuleNotFound
 try:
    import numpy
    print("Module found")
except:
    print("Module not found")
   

#ValueError
    try:
    a = int(input("Enter the number"))

except:
    print("Its not a number")

#ZeroDivisionError
try:
    c=2/0
    print(c)
except:
    print("Cannot divide by zero")

#2)Design a simple calculator app with try and except for all use cases
   
print("Choose the arithmetic function you want to do:")
print("Enter 1 to perform addition")
print("Enter 2 to perform subtraction")
print("Enter 3 to perform multiplication")
print("Enter 4 to perform division")
try:
    ans = int(input("Enter your choice : "))
    if ans==1:
        a = float(input("Enter the first integer : "))
        b = float(input("Enter the second integer : "))
        print(a+b)
    elif ans==2:
        a = float(input("Enter the first integer : "))
        b = float(input("Enter the second integer : "))
        print(a-b)
    elif ans==3:
        a = float(input("Enter the first integer : "))
        b = float(input("Enter the second integer : "))
        print(a*b)
    elif ans==4:
        a = float(input("Enter the first integer : "))
        b = float(input("Enter the second integer  : "))
        print(a/b)
    else:
        print("Enter a valid integer.")
except NameError:
    print("Please use numbers only.")
except SyntaxError:
    print("Please use numbers only.")
except TypeError:
    print("Please use numbers only.")
except AttributeError:
    print("Please use numbers only.")
except ValueError:
    print("Please use numbers only.")  

#3)Print one message if the try block raises a NameError and another for other errors
try:
    raise NameError("Good")
except NameError:
    print("The Exception is handled")

#4)When try-except scenario is not required
#Answer:Whwenever there is no need for error to be handled or we can let the program to display the error,try-except scenario is not required.

#5)Try getting an input inside the try catch block
while True:
    try:
        x=int(input("Enter the integer:"))
        print("The integer you have entered is",x)
        break
    except:
        print("Invalid integer")
print("Successfully entered")
