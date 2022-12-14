#1)Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},

from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result) 
print("--------------------------------------!------------------------------------------")

#2)Write a Python program to combine two dictionary adding values for common keys.

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)
print("--------------------------------------!------------------------------------------")

#3)How will you compare two lists?
"""
Method 1: Compare Two Lists Using Equal Sign Operator.
Method 2: Match Data by Using Row Difference Technique.
Method 3: Match Row Difference by Using IF Condition.
Method 4: Match Data Even If There is a Row Difference.
Method 5: Highlight All the Matching Data using Conditional Formatting.
"""
print("--------------------------------------!------------------------------------------")

#4)Write a Python program to calculate surface volume and area of a cylinder

pi=22/7
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = pi * radian * radian * height
sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)
print("--------------------------------------!------------------------------------------")

#5)Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

#from decimal import *
data = list(map('2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))
print("--------------------------------------!------------------------------------------")

#6)Write a Python program to convert degree to radian

pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)
print("--------------------------------------!------------------------------------------")

#7)How Do You Traverse Through A Dictionary Object In Python?
"""
There are two ways of iterating through a Python dictionary object. 
One is to fetch associated value for each key in keys() list. 
There is also items() method of dictionary object which returns list of tuples, each tuple having key and value.
"""
print("--------------------------------------!------------------------------------------")

#8)Differentiate between append () and extend () methods?
"""
ans :Python append() method adds an element to a list, and the extend() method concatenates the first list with another list (or another iterable).
When append() method adds its argument as a single element to the end of a list, the length of the list itself will increase by one
"""
print("--------------------------------------!------------------------------------------")

#9)Write a Python program to split a list into different variables

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1, var2, var3 = color
print(var1)
print(var2)
print(var3)
print("--------------------------------------!------------------------------------------")

#10)Write a Python program to returns sum of all divisors of a number

def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(8))
print(sum_div(12))
print("--------------------------------------!------------------------------------------")

#11)Write a Python program to remove an empty tuple(s) from a list of tuples

L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)
print("--------------------------------------!------------------------------------------")

#12)Write a Python function to calculate the factorial of a number (a non-negative integer)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
print("--------------------------------------!------------------------------------------")

#13)Write a Python function to get the largest number, smallest num and sum of all from a list.

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))
print("--------------------------------------!------------------------------------------")

#14)Write a Python program to check a list is empty or not

l = []
if not l:
  print("List is empty")
  print("--------------------------------------!------------------------------------------")

#15)Write a Python function that takes two lists and returns true if they have at least one common member

def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
print("--------------------------------------!------------------------------------------")

#16)Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()
print("--------------------------------------!------------------------------------------")

#17)Write a Python function that takes a list and returns a new list with unique elements of the first list

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 
print("--------------------------------------!------------------------------------------")

#18)How do you perform pattern matching in Python? Explain
"""
ans :Import the regex module with import re.
Create a Regex object with the re. compile() function. ...
Pass the string you want to search into the Regex object's search() method. ...
Call the Match object's group() method to return a string of the actual matched text.
"""
print("--------------------------------------!------------------------------------------")
#18)
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)
print("--------------------------------------!------------------------------------------")

#19)from sqlite3.dbapi2 import _Statement

"""
1.function:which is declare outside the class function are independent
           def my fun():
            Statement
2.method:which is declare inside the class methods are dependent on class-object

  def myfun():
    Statement
     
      """
print("--------------------------------------!------------------------------------------")

#20)Write a Python function that checks whether a passed string is palindrome or not

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
print("--------------------------------------!------------------------------------------")

#21)Write a Python program to calculate the area of a parallelogram

base_1 = 5
base_2 = 6
height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)
print("--------------------------------------!------------------------------------------")

#22)Write a Python function to check whether a number is perfect or not.

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))
print("--------------------------------------!------------------------------------------")

#23)Write a Python script to sort (ascending and descending) a dictionary by value.

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
print("--------------------------------------!------------------------------------------")

#24)Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
print("--------------------------------------!------------------------------------------")

#25)Write a Python script to check if a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
print("--------------------------------------!------------------------------------------")

#26)Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)  
print("--------------------------------------!------------------------------------------")

#27)Write a Python program to read a random line from a file.
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('test.txt'))
print("--------------------------------------!------------------------------------------")

#28)Write a Python program to select an item randomly from a list.

import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))
print("--------------------------------------!------------------------------------------")

#29)Write a Python program to find the repeated items of a tuple

#create a tuple
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
print(tuplex)
#return the number of times it appears in the tuple.
count = tuplex.count(4)
print(count)
print("--------------------------------------!------------------------------------------")

#30)Write a Python program to reverse a tuple

#create a tuple
x = ("w3resource")
# Reversed the tuple
y = reversed(x)
print(tuple(y))
#create another tuple
x = (5, 10, 15, 20)
# Reversed the tuple
y = reversed(x)
print(tuple(y))
print("--------------------------------------!------------------------------------------")

#31)Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string. Sample string: 'w3resource

from collections import defaultdict, Counter
str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)
print("--------------------------------------!------------------------------------------")

#32)Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
print("--------------------------------------!------------------------------------------")

#33)Write a Python program to find the second smallest number in a list.

def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()    
  return  uniq_items[1]   

print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2,2]))
print(second_smallest([2]))
print("--------------------------------------!------------------------------------------")

#34)Write a Python program to convert a list of characters into a string.

s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)
print("--------------------------------------!------------------------------------------")

#35)Write a Python program to check whether a list contains a sub list

def is_Sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True

	return sub_set

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))
print("--------------------------------------!------------------------------------------")

#36)Write a Python program to get unique values from a list

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)
print("--------------------------------------!------------------------------------------")

	






