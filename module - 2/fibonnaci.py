# write a program to get a fibonnaci series the given number

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