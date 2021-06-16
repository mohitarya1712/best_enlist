#day_4_exercise

#1.Write a program to create a list of n integer values and do the following
l = [1,7,1,2]
print(l)

#Add an item in to the list (using function)
# using append()
l.append(4)
print(l)

#using insert()
l.insert(5,5)
print(l)


#Delete (using function)
#using pop()
l.pop()
print(l)

#using remove()
l.remove(4)
print(l)

#Store the largest number from the list to a variable
m = max(l)
print(m)

#Store the Smallest number from the list to a variable
n = min(l)
print(n)

#2.create a tuple and print the reverse of the created tuple

t = (6, 7, 8, 9 )
print(t)

#using slicing technique
print(t[::-1])

#using reversed() function
r = reversed(t)
print(tuple(r))

#3.Create a tuple and convert tuple into list
t2 = (4, 5, 6, 7)
print(t2)
print(type(t2))

l2 = list(t2)
print(l2)
print(type(l2))
