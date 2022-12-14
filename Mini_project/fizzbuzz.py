def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            print('fizzbuzz',end=' ')
        elif i%3==0:
            print("Fizz",end=' ')
        elif i%5==0:
            print("Buzz",end=' ')
        else:
            print(i,end=' ')
fizzbuzz(20)

"""
n=int(range(1,21))
#n=(int(input("Enter number: ")))
for i in range (n):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print('Fizz')
    else:
        i%5==0
        print("Buzz")
print(i)


#n=(int(input("Enter number: ")))
for i in range (1,n+1):
    if n%3==0 and n%5==0:
            print('fizzbuzz')
    elif n%3==0:
            print('Fizz')
    else:
            n%5==0
            print("Buzz")
    print(n)
"""