#  Write a python program to test whether a passed letter is vowel or not

A = int(input("enter a alphabet:"))
if A in ('a','e','i','o','u'):
    print("this letter is vowel")
elif A =='y':
    print("sometimes letter y stand for vowel,sometimes stand for constant:")
else:
    print("this letter is not vowel")