                                         modul- 3

#1).   What is List? How will you reverse a list?
#Ans.  Lists are used to store multiple items in a single variable.
#      Using the reversed() method and reverse() method , we can reverse the contents of the list object in place i.e., 
#      we don't need to create a new list instead we just copy the existing elements to the original list in reverse order. 
#      This method directly modifies the original list.
#2). How will you remove last object from a list?
#    Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
#Ans.Is remove last object from a list using pop() method
a = [2,33,222,14,25]
a.pop()
a = a[-1]
print(a)

#3).  Differentiate between append () and extend () methods?
#Ans. 
    #append()    The append() method appends an element to the end of the list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Appebd Eg.",fruits)

    #extend()    The extend() method adds the specified list elements (or any iterable) to the end of the current list.
fruits = ['apple', 'banana', 'cherry']  
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print("Extend Eg.",fruits)


#4).Write a Python function to get the largest number, smallest num and sum of all from a list.

mylist = [10,50,40,32,60]
print("My largest number in a list is : ", max(mylist))
print("My samllest number in a list is : ",min(mylist))
print("Mylist element totel of: ",sum(mylist))

#4).How will you compare two lists?
"""Ans. Python sort() method and == operator to compare lists
We can club the Python sort() method with the == operator to compare two lists. 
Python sort() method is used to sort the input lists with a purpose that if the two input lists are equal, 
then the elements would reside at the same index positions."""
#5).Write a Python program to count the number of strings where the string length is 2 or more and 
#   the first and last character are same from a given list of strings.

l = ['aba','101','cbc','abc','abc','aba']
count=0
for i in l:
  l1=len(i)
  if l1>1 and i[0]==i[-1]:
   count+=1
print(count)

#6).Write a Python program to remove duplicates from a list.
data=[10,20,20,10,60,40,405,45,20,15,55]
noduplicat = []
def remove_duplicates(duplicat):
  for element in duplicat:
    if element not in noduplicat:
      noduplicat.append(element)
  return noduplicat 
print(remove_duplicates(data))

#5).Write a Python program to check a list is empty or not.
list = []
if not list:
  print("list is empty")
else:
  print("list is not empty")

#6).Write a Python function that takes two lists and returns true if they have at least one common member.
list1 = [1,2,3,4,5,6]
list2 = [1,6,5,4,7,8,9,10]
for x in list1:
  for y in list2:
    if(x==y):
       print(True)

#7).Write a Python program to generate and print a list of first and last 5 elements 
#   where the values are square of numbers between 1 and 30.

list = []
for i in range(1,31):
  list.append(i**2)
print(list[:5])
print(list[-5:])

#8).Write a Python function that takes a list and returns a new list with unique elements of the first list.
list = [10,20,30,10,20,60,50,50,40,20,30,10,10,10]
unique_list = []
for i in list:
  if i not in unique_list:
    unique_list.append(i)
print("Unique list : ",unique_list)

#9).Write a Python program to convert a list of characters into a string.
list1 = ['h','e','l','l','o']
list = ''.join(list1)
print(list)

#10).Write a Python program to select an item randomly from a list

import random
mylist = [10,20,30,40,'karan','car']
random.choice(mylist)

#11).Write a Python program to find the second smallest number in a list.

list =[10,20,30,50,60,15,22,23,25]
list.sort()
print(list)
print("My smallest number in a list is : ",list[1])
[10, 15, 20, 22, 23, 25, 30, 50, 60]
#12).Write a Python program to get unique values from a list
list = [10,20,30,10,5,4,8,9,9,5,4,8,10]
unique_list = []
for i in list:
  if i not in unique_list:
    unique_list.append(i)
print("Unique list : ",unique_list)

#13). Write a Python program to check whether a list contains a sub list
list = [10,2,5,60,50,10,2,30,40]

l =input("Enter a list 1 number : ")
l1 =input("Enter a list 2 number : ")
if (all(i in l for i in l1)):
  print("Sublist is present in list")
else:
  print("Sublist is not present in list")

#14).Write a Python program to split a list into different variables.
list = ['Red','Blue','Yellow']
print("List : ",list)

a,b,c = list
print("a",a)
print("b",b)
print("c",c)


#15). What is tuple? Difference between list and tuple
#Ans. Tuples are used to store multiple items in a single variable.
#     The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable.
#     This means that tuples cannot be changed while the lists can be modified. 
#     Tuples are more memory efficient than the lists.
#16).Write a Python program to create a tuple with different data types.
a = ['abc',10,True,50,3.5]
b = tuple(a)
print(b)
('abc', 10, True, 50, 3.5)
#17).Write a Python program to create a tuple with numbers.
a = (12,13,11,110,111)
print(a)

b = input("Enetr the number :")

print(b)
(12, 13, 11, 110, 111)

#18).Write a Python program to convert a tuple to a string.

tup = ('H','E','L','L','O')
str = ''

for i in tup:
  str = str + i
print(str)

#19).Write a Python program to check whether an element exists within a tuple.

tup=(10,20,50,6,40,80,'apple','abc')
print(10 in tup)
True
#20).Write a Python program to find the length of a tuple.

tup = (10,50,40,60,20)

length = len(tup)
print(tup)
print("Tuple length is : ",length)
(10, 50, 40, 60, 20)

#21).Write a Python program to convert a list to a tuple.

list = [10,2,5,6,70,9,70,800,50,40]
print("List number of value: ",list)

a = tuple(list)
print("Convert list to tuple value:",a)

#22).Write a Python program to reverse a tuple.
x = str("hello")
y = reversed(x)
y1=tuple(y)
print(y1)
('o', 'l', 'l', 'e', 'h')
#23.Write a Python program to replace last value of tuples in a list.

a = [(10,20,30),(100,200,300),(1,2,3)]
for l in a :
  print([l[:-1] + (1000,)])
[(10, 20, 1000)]
[(100, 200, 1000)]
[(1, 2, 1000)]
#24.Write a Python program to find the repeated items of a tuple.
t = (1,2,5,6,9,9,9,98,8,5,5,5,2,2,2,1,10,11,10,12)
count = t.count(9)
print("Find the repeated items number :-",count)

#25.Write a Python program to remove an empty tuple(s) from a list of tuples.
a = [(), (),('a'),("a,b"),("a,c,d,b")]
a = [l for l in a if l]
print(a)
['a', 'a,b', 'a,c,d,b']
#26.Write a Python program to unzip a list of tuples into individual lists.
a = [(10,20),(40,50),(70,80)]
print(a)
def unziplist(a):
  for i in a:
    c=list(i)
    print(c)
unziplist(a)
[(10, 20), (40, 50), (70, 80)]
[10, 20]
[40, 50]
[70, 80]
#27.Write a Python program to convert a list of tuples into a dictionary.
list1=[("apple",90),("banana",60)]
dict1={}
for name , marks in list1:
  dict1.setdefault(name,[]).append(marks)
print(dict1)
{'apple': [90], 'banana': [60]}
#28. How will you create a dictionary using tuples in python?
tuple=(('age',25),('boyage',22),('girlage',21))
print(tuple)
dec = dict((y, x)for x ,y in tuple)

print(dec)
(('age', 25), ('boyage', 22), ('girlage', 21))
{25: 'age', 22: 'boyage', 21: 'girlage'}
#29).Write a Python script to sort (ascending and descending) a dictionary by value.
di = {100:5,17:4,60:3,90:2}
print("Original vlaue : ",di)
sort = sorted(di.items())
print(sort)

[(17, 4), (60, 3), (90, 2), (100, 5)]
#30).Write a Python script to concatenate following dictionaries to create a new one.
a = {"car":600000}
b = {"bike":75000}
c = {"activa":63000}
d = {}
for i in (a,b,c):
  i.update(d)
  print(i)
{'car': 600000}
{'bike': 75000}
{'activa': 63000}
#31).Write a Python script to check if a given key already exists in a dictionary.
a = {100:1,200:2,300:3}
def key(b):
 if b in a:
   print("Key is present in the dictionary")
 else:
   print("Key is not present in the dictionary")
key(200)
key(1)

#32).How Do You Traverse Through A Dictionary Object In Python?
class dictObj(object):
     def __init__(self):
         self.x = 'red'
         self.y = 'Yellow'
         self.z = 'Green'
     def do_nothing(self):
         pass
test = dictObj()
print(test.__dict__)
{'x': 'red', 'y': 'Yellow', 'z': 'Green'}
#33).How Do You Check The Presence Of A Key In A Dictionary?
check = {'car':'varna','bike':'bullet','rahul':'car dirver'}
user = (input("Enter key you want to check:-"))
if user in check:
  print("the key is present")
else:
  print("The key is not present")

#34).Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
a = dict()
for i in range(1,16):
  a[i]=i**2
print(a)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
#35).Write a Python program to check multiple keys exists in a dictionary
di = {
    'apple' : 'red',
    'banana': 'yellow',
    'kiwi'  : 'coffee'
}
print(di.keys()>={'apple','banana'})
print(di.keys()>={'apple','red'})
print(di.keys()>={'kiwi','yellow'})
True
False
False
#36).Write a Python script to merge two Python dictionaries.
a = {'a':100,'b':200,'c':300}
b = {'d':400,'e':500}
c  = a.copy()
c.update(b)
print(c)
{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
#37).Write a Python program to map two lists into a dictionary.
keys = ['red' , 'yellow','blue']
values = ['#FF0000','#008000', '#0000FF']
color = dict(zip(keys,values))
print(color)
{'red': '#FF0000', 'yellow': '#008000', 'blue': '#0000FF'}
#38).Write a Python program to combine two dictionary adding values for common keys.
#    d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,???d???:400}
#    Sample output: Counter ({'a': 400, 'b': 400,???d???: 400, 'c': 300}).

d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d1:
  if key in d2:
    d2[key] = d1[key]+d2[key]
  else:
    d2[key]=d1[key]
print(d2)
{'a': 400, 'b': 400, 'd': 400, 'c': 300}
#39).Write a Python program to print all unique values in a dictionary.
name = {1:'raj',2:'chintu',3:'lalo',4:'raj',5:'chintu'}
print(name)
print(set(name.values()))
{1: 'raj', 2: 'chintu', 3: 'lalo', 4: 'raj', 5: 'chintu'}
{'raj', 'lalo', 'chintu'}
#40).Why Do You Use the Zip () Method in Python?
#Ans.Python's zip() function creates an iterator that will aggregate elements from two or more iterables. 
#    You can use the resulting iterator to quickly and consistently solve common programming problems, 
#    like creating dictionaries
#Ex.
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
list(zip(s1, s2))
[(1, 'b'), (2, 'a'), (3, 'c')]
#41).Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
#    Sample data: {'1': ['a','b'], '2': ['c','d']}
#    Expected Output:
0#                    ac ad bc bd
sampledata = {'1': ['a','b'], '2': ['c','d']}
l = list(sampledata.values())
for i in l[1:]:
  for j in l[0]:
    for k in i:
      print(j+k,end=" ")

#42).Write a Python program to find the highest 3 values in a dictionary.
price = {'belt':1000,'Tshirt':600,'pent':1200,'shoes':1500}
a = sorted(price, key=price.get,reverse=True)
for i in range(3):
  print(a[i])

#43).Write a Python program to combine values in python list of dictionaries.   
#    Sample data:[{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}]
#    Expected Output:
#    Counter ({'item1': 1150, 'item2': 300})
from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result)
Counter({'item1': 1150, 'item2': 300})
#44).Write a Python program to create a dictionary from a string.
#    Note: Track the count of the letters from the string.
#    Sample string: 'w3resource'
#    Expected output:
#    {'3': 1,???s???: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)
{'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
#45.Write a Python function to calculate the factorial of a number (a nonnegative integer)
def factorial(n):
  if n==0:
    return 1
  else:
    return n * factorial(n-1)
n = int(input("Input a number to compute the factiorial :"))
print(factorial(n))

120
#46).Write a Python function to check whether a number is in a given range.
def test(n):
  if n in range(2,10):
    print("%s Is in the range"%str(n))
  else:
    print("Is not in the range")
test(6)
test(15)

#47).Write a Python function to check whether a number is perfect or not.
def perfect(n):
  sum = 0
  for i in range(1,n):
    if n%i==0:
      print(i)
      sum=sum+i
  return sum
n = int(input("Enter the number:-"))
s = perfect(n)
if n==s:
  print("The number enter by you is perfect number")
else:
  print("The number enter by you is not perfect number")

#48).Write a Python function that checks whether a passed string is palindrome or not.
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('aza'))
True
#49).How Many Basic Types Of Functions Are Available In Python?
#Ans).  
#      1)Built-in functions:Built-in functions are the functions that are already written or defined in python. We only need to remember the names of built-in functions and the parameters used in the functions. 
#        As these functions are already defined so we do not need to define these functions. Below are some built-in functions of Python.
#EX:
x = [1,2,3,4,5]
print(len(x))    #it return length of list
print(type(x))
#      2)user-defined functions:The functions defined by a programmer to reduce the complexity of big problems and to use that function according to their need. 
#       This type of functions is called user-defined functions.
#EX:
x = 3
y = 4
def add():
    print(x+y)
    
add()

#50).How can you pick a random item from a list or tuple?
import random
list = [10,20,30,40,50,60]
tuple = ("xyz","yzx","zyx")
print(random.choice(list))
print(random.choice(tuple))


#51:How can you pick a random item from a range?
#Ans. Use a random. randrange() function to get a random integer number from the given exclusive range by specifying the increment. 
#     For example, random. randrange(0, 10, 2) will return any random number between 0 and 20 (like 0, 2, 4, 6, 8)
import random

for i in range(1,10):
  y=random.randrange(9)
  print(y,end=" ")
 
#52).How can you get a random number in python?
#Ans.To generate random number in Python, randint() function is used. This function is defined in random module.
#53).How will you set the starting value in generating random numbers?
#Ans.The random number generator needs a number to start with (a seed value), to be able to generate a random number. 
#    By default the random number generator uses the current system time. Use the seed() method to customize the start number of the random number generator.
#54).How will you randomizes the items of a list in place?
import random
list = [10,20,30,40,50,60,70]
random.choice(list)
30
#55).Write a Python program to read a random line from a file.
import random
def readrandomline():
  f=open("p.txt","r")
  lines=f.randomlines()
  length=len(lines)
  r1=random.randint(0,length-1)
  print(lines[r1])
  f.close()
readrandomline()



#56).Write a Python program to convert degree to radian.
pi = 22/7
degree = float(input("provide input deggree:"))
radian = degree*(pi/180)
print("the value of radian",radian)


#57).Write a Python program to calculate the area of a trapezoid.
h = float(input("Height of trapezoid: "))
b1= float(input("Base of the first value: "))
b2= float(input("Base of the second value: "))
area = ((b1+b1)/2)*h
print("Area of teapezoid is" , area)

#58).Write a Python program to calculate the area of a parallelogram.
l = float(input("Enter length of parallelogram: "))
w= float(input("Enter width of parallelogram: "))
h= float(input("Enter height of parallelogram: "))
area = l*h
perimeter = 2*l+2*w
print("Area of parallelogram is: ",area)
print("Area of parallelogram is: ",perimeter)

#59).Write a Python program to calculate surface volume and area of a cylinder.
pi = 22/7

r= float(input("Enter redius of cylinder: "))
h= float(input("Enter height of cylinder "))
volume =pi*r*r*h
surface = ((2*pi*r)*h)+((pi*r**2)*2)
print("Voluem is :",volume)
print("Surface is : ",surface)

#60).Write a Python program to returns sum of all divisors of a number.
a=int(input("Please enter a number : "))
def divisors(a):
  fa=[]
  for i in range(1,a+1):
    if a%i==0:
      fa.append(i)
  print(fa)
  print(f"The sum of divisors of {a} is ",sum(fa))
divisors(a)

#61).Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
data = [2.45, 2.69, 2.45, 3.45, 2.00, 0.04, 7.25]
print("Maximum: ", max(data))
print("Minimum: ", min(data))


