#Exercise day 7:

#1. Create a function getting two integer inputs from user. & print the following:
def math(x,y):
    print('Addition of two numbers is',x+y)
    print('Subtraction of two numbers is', x-y)
    print('Division of two numbers is', x/y)
    print('Multiplication of two numbers is', x*y)

x = int(input("Enter first number: "))
y = int(input("Enter first number: "))
math(x,y)

#2. Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree
def covid(name, temp = 98):
    print('Patient name:',name)
    print('Body temperature:',temp)

covid('ram',100)
covid('shyam')
