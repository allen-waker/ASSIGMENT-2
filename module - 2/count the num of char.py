#Write a Python program to count the number of characters (character frequency) in a string
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