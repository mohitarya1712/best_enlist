#Write a Python script to merge two Python dictionaries.
dict1 = {1:'a', 2:'b', 3:'c', 4:'d'}
dict2 = {5:'e', 6:'f', 7:'g', 8:'h'}
print('Dictionary 1:', dict1)
print('Dictionary 2:', dict2)
dict3 = dict1.copy()
dict3.update(dict2)
print('Merged dictionary:', dict3)

#Write a program to sort the value from descending to ascending in list and convert it in to a set.
list1 = [6, 2, 9, 4, 5, 1, 7, 8, 3]
print('\nList: ', list1)
#sorting list
list1.sort(reverse = True)
print('Sorted list:', list1)
#typecasting to set
set1 = set(list1)
print('Set:', set1)

# Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.
dict4 = {5:'e', 6:'f', 7:'g', 8:'h',1:'a', 2:'b', 3:'c', 4:'d'}
keys1 = list(dict4.keys())
print('\nKeys in dictionary:', keys1)
#sorting with function
keys1.sort()
print('Sorted keys with function:',keys1)
#sorting without function
keys2 = keys1.copy()
sort = []

while keys2:
    min = keys2[0]  
    for x in keys2: 
        if x < min:
            min = x
    sort.append(min)
    keys2.remove(min)

print('Sorted keys without function:', sort)

#Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.
s = input('\nEnter string: ')
o = input('Enter the word you want to replace: ')
u = input('Enter the word you want to be replaced with: ')
print('Replaced String:',s.replace(o,u,1))

#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.
s1 = input('\nEnter string:')
char = s1[0]
print('Replaced string:',s1.replace(char, char.capitalize()))

#Write a Python program to find the repeated items of a list
l=[1,2,4,4,5,6,7,7,9,9]
print('\nList:', l)
l1=[]
print('Repeated items:')
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')

#Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user
elements = 100, 200, 400
print('\n\nElements:', elements)
Sum = (sum(elements))
print('Sum:', Sum)
v = int(input('Enter divisor:'))
print('Answer:',Sum/v)

#Write a Python program to find the Mean, median, mode among three given numbers
#mean
numbers = [2, 4, 8]
print('\nNumbers:', numbers)
Sum1 = sum(numbers)
n = len(numbers)
mean = Sum1/n
print('Mean:', mean)
#median
numbers.sort()
  
if n % 2 == 0:
    median1 = numbers[n//2]
    median2 = numbers[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = numbers[n//2]
    
print("Median :", median)
#mode
import statistics
print('Mode:', statistics.mode(numbers))

#Write a Python program to swap cases of a given string
string = "The quick brown fox jumps over the lazy dog"
print('\nString:', string)
print('Swapcased string:', string.swapcase())

#Write a program to convert an integer to binary & octa decimal
integer = 123
print('\nInteger:', integer)
print('Binary:', bin(integer))
print('Octal:', oct(integer))
