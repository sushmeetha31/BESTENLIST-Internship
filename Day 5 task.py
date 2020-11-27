#DAY 5 TASK
#Create a function getting two integer inputs from user & print the following:

#Addition of two numbers is +value
#Subtraction of two numbers is +value
#Division of two numbers is +value
#Multiplication of two numbers is +value

#Here the value represents math function associated
def f(a,b):
    print("Addition of two numbers is",a+b)
    print("Subtraction of two numbers is",a-b)
    print("Multiplication of two numbers is",a*b)
    print("Division of two numbers is",a//b)
a = int(input("First number: "))
b = int(input("Second number: "))
f(a,b)


#Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree
def covid(name,temp=98):
    print("Patient name : ",name)
    print("Temperature : ",temp)
x = input("Enter patient name:")
y = input("Enter body temperature:")
covid(x,y)
