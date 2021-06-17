#Day 5 Exercise (Dictionary,Sets)

#1. Write a Python script to merge two Python dictionaries
dict1 = {1: 'a', 2: 'b'}
print(dict1)

dict2 = {3: 'c', 4: 'd'}
print(dict2)

#Using copy() and update()
dict3 = dict1.copy()
dict3.update(dict2)

print(dict3)

#2. Write a Python program to remove a key from a dictionary
#using del
del dict3[1]
print(dict3)

#using popitem()
dict3.popitem()
print(dict3)

#using pop()
dict3.pop(3)
print(dict3)

#3. Write a Python program to map two lists into a dictionary
keys = [1, 2, 3, 4]
values = ['a', 'b', 'c', 'd']
dict4 = dict(zip(keys, values))
print(dict4)

#4. Write a Python program to find the length of a set
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
print(set1)

#using len()
print(len(set1))

#5. Write a Python program to remove the intersection of a 2nd set from the 1st set
set2 = {7, 8, 9, 0}

#using intersection()
set3 = set1.intersection(set2)
print(set3)
