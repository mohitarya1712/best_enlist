#Write a program to loop through a list of numbers and add +2 to every value to elements in list
list1 = [1, 4, 9, 44, 77, 99]
print("List:", list1)
for i in range(len(list1)):
    list1[i] += 2
print("List after adding 2 to elements:", list1, '\n')

#Write a program to get the below pattern
''' 54321
    4321
    321
    21
    1
'''

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

#Python Program to Print the Fibonacci sequence
nterms = int(input("\nEnter no of terms: "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Enter a positive integer: ")
elif nterms == 1:
   print("Fibonacci sequence:",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

#Explain Armstrong number and write a code with a function
'''
A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.
The Armstrong number is also known as narcissistic number.
'''
num = int(input("\nEnter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#Write a program to print the multiplication table of 9
print('\nMutiplication table of 9:')
for i in range(1, 11):
   print(9, 'x', i, '=', 9*i)

# Check if a program is negative or positive
number = float(input("\nEnter a number: "))
if number > 0:
   print(number, "is a positive number")
else:
   print(number, "is a negative number")

#Write a program to convert the number of days to ages
days = int(input("\nEnter number of days: "))
years = int(days / 365)
print("No of years:", years)

#Solve Trigonometry problem using math function write a program to solve using math function
import math

def trig(n, m):
    if n == 'sin':
        print("\nSine of ", m, " is", math.sin(m))
    elif n == 'cos':
        print("Cosine of ", m, " is", math.cos(m))
    elif n == 'tan':
        print("Tangent of ", m, " is", math.tan(m))
    elif n == 'sec':
        print("Secant of ", m, " is", (1 / math.cos(m)))
    elif n == 'cosec':
        print("Cosecant of ", m, " is", (1 / math.sin(m)))
    elif n == 'cot':
        print("Cotangent of ", m, " is", (1 / math.tan(m)))


trig("sin", 90)
trig("cos", 90)
trig("tan", 90)
trig("cosec", 90)
trig("sec", 90)
trig("cot", 90)

#Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
print("\nCalculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

ch = int(input("Enter Choice(1-4): "))

if ch == 1:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c=a + b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")
