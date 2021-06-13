#STRING PRACTICE

#print a value
print("30 days 30 hour challenge")  #double quotes
print('30 days 30 hour challenge')  #single quotes

#assigning string to variable
Hours = "thirty"
print(Hours)        #prints "thirty"

#indexing using string
Days = "Thirty days"
print(Days[0])      #prints "T"
print((Days[5]))    #prints "y"

#print particular chracter form certain text
Challenge = "I will win"
print(Challenge[7:10])  #prints "win"
print(Challenge[0:7])   #prints "I will"

#print the length of the character
print(len(Challenge))   #prints "10"

#convert string into lower chracter
print(Challenge.lower())    #prints "i will win"

#convert string into upper chracter
print(Challenge.upper())    #prints "I WILL WIN"

#string concatenation: joining two strings
a = "30 days"
b = "30 hours"
c = a + b
print(c)    #prints "30 days30 hours"

#adding space during concatenation
c = a + " " + b
print(c)    #prints "30 days 30 hours"

#casefold(): #makes the string lowercase
text = "Thirty days and Thirty Hours"
x = text.casefold() 
print(x)    #prints "thirty days and thirty hours"

#capitalize(): upper case the first letter
t = "DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
print(t.capitalize())    #prints "Don’t trouble trouble until trouble troubles you"

#find(): finds the first occurrence of the specified value
print(t.find("T"))   #prints "4"

#isalpha(): returns True if all the characters are alphabet
print(t.isalpha())   #prints "False"
y = "mohitarya"
print(y.isalpha())      #prints "True"

#isalnum(): returns True if all the characters are alphanumeric
print(t.isalnum())   #prints "False"
z = "mohitarya1712"
print(z.isalnum())  #prints "True"
