#1) Write a Python program to count occurrences of a substring in a string.

str1 = 'python is a pouplar language.'
print()
print(str1.count("popular"))
print()
print("-------------------------!--------------------------------------------")

#-------------------------!--------------------------------------------
#3)Write a Python program to get a single string from two given strings,separated by a space and swap
#  the first two characters of each string.
def chars_mix_up(a,b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a +' ' + new_b
print(chars_mix_up('abc','xyz'))
print("-------------------------!--------------------------------------------")

#4)Write a Python program to count the number of characters (character frequency) in a string
n = input("enter the string:").lower()
s = {}
for i in n:
    if i in s:
        s[i]+1
    else:
        s[i]=1
print(s)


"""
What are negative indexes and why are they used?
ans: you can use negative indexing as your advantages when you want to pick a values from the end(right side)
of an iterable.

"""
print("-------------------------!--------------------------------------------")

 #5) write a program to find whether a given number is even of odd

num = int(input("enter the a number: "))
if (num % 2)==0:
    print("even number")
else:
    print("odd number")  
print("-------------------------!--------------------------------------------")

#6) write a program to get the factorial number of a given number

class program:

    def checkfactorial(self):
        f = 1
        for i in range(1,num+1):
            f*=1

        print("factorial = ",f)

obj = program
num = int(input("enter a number : "))
obj.checkfactorial(num)
print("-------------------------!--------------------------------------------")

#7) write a program to get a fibonnaci series the given number

num = int(input("enter the number: "))
n1,n2 = 0,1
print("fibonnaci series",n1,n2,end=" ")
for i in range(2,num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end =" ")
print()

""""
How memory is managed in Python?
Ans: python uses the dynamic memory allocation which is managed by the heap data structure.

What is the purpose continue statement in python?
Ans: The continue keyword is used to end the current iteration in a for loop or while loop and continues 
to the next iteration.
"""
print("-------------------------!--------------------------------------------")

#8)Write a Python function that takes a list of words and returns the length of the longest one

def main():
    text = input("please enter a list of words to evaluate:")
    
    longest = 0
    for words in text.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words
    print("the longest word is",longest_word,"with length",len(longest_word))
main()   
print("-------------------------!--------------------------------------------")

#9)Write a Python program to calculate the length of a string

str = input("enter a string:")
counter = 0
for s in str:
    counter = counter +1
print("length of the input string is:",counter)

def myfun():
  l1 = ['a','i','o','u','e']

  ch = input("Enter character : ").lower()
  if ch in l1:
    print("vowel")
  else:
    print("invalid vowel")
    myfun()
print("-------------------------!--------------------------------------------")

 #10) write a program to check if a number is positive, negative or zero

num = int(input("enter the number:"))
if num>0:
    print("positive number")
elif num ==0:
    print("zero")
else:
    print("negative number")
print("-------------------------!--------------------------------------------")


 #11)Write a python program to sum of the first n positive integers
num = int(input("enter the number: "))
total = num * (num + 1)/2
print("the sum of the first", num," positive integers",total)  
print("-------------------------!--------------------------------------------")

#12)Write a Python function to reverses a string if its length is a multiple of 4

def reverse_string(str1):
    if len(str1) % 4 ==0:
        return ''.join(reversed(str1))
        return str1

print(reverse_string('abcd'))
print(reverse_string('python'))
print("-------------------------!--------------------------------------------")

#13)Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string

def string_both_ends(str):
    if len(str) <2:
        return ' '
    return str[0:2] + str[-2:]

print(string_both_ends('w3basharat'))
print(string_both_ends('w3'))
print(string_both_ends('w'))
print("-------------------------!--------------------------------------------")

#14)
def myfun():
  l1 = ['a','i','o','u','e']

  ch = input("Enter character : ").lower()
  if ch in l1:
    print("vowel")
  else:
    print("invalid vowel")
    myfun()
print("-------------------------!--------------------------------------------")

#15)Write a Python program to sum of three given intergers.However, if two values are equal sum will be zero

def sum_three(x,y,z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum
    
print(sum_three(2,1,2))
print(sum_three(3,2,2))
print(sum_three(2,2,2))
print(sum_three(1,2,3))
print("-------------------------!--------------------------------------------")

#16) write a program that swap two number with temp variable and without temp variable

x = 20
y = 40
temp = x
x= y 
y = temp

print("value of x: ",x)
print("value of y: ",y)
print("-------------------------!--------------------------------------------")

#17)Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string
# is less than 3, leave it unchanged

def add_string(str1):
    length = len(str1)

    if length > 2:
        if str1[-3:] =='ing':
           str1+= 'ly'
        else:
            str1 += 'ing'
    return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
print("-------------------------!--------------------------------------------")


#18)Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
#  if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
#  Return the resulting string

def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot>0 and spoor>0:
        str1 = str1.replace(str1[snot:(spoor+4)],'good')
        return str1
    else:
        return str1
print(not_poor('the lyrics is not that poor!'))
print(not_poor('the lyrics is poor!'))
print("-------------------------!--------------------------------------------")


# 19) Write a python program to test whether a passed letter is vowel or not

A = int(input("enter a alphabet:"))
if A in ('a','e','i','o','u'):
    print("this letter is vowel")
elif A =='y':
    print("sometimes letter y stand for vowel,sometimes stand for constant:")
else:
    print("this letter is not vowel")
print("-------------------------!--------------------------------------------")





