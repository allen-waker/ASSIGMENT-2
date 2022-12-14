
def prime(n):
    f=False
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                f = True
                break
    if f:
        print("No ! its not a prime number")
    else:
        print("Yes ! its a prime number")
n=50
print(prime(n))


def  p(m):
    if m>1:
        for i in range(2,m//2+1):
            if m%i==0:
                print("No its not a prime number")
                break
            else:
                print("Yes its a prime number")
        else:
            print("No! ITs not a prime number")
m=10
p(m)



def  p(start,end):
    for s in range(start,end):
        if s>1:
            for i in range(2,s//2+1):
                if s%i==0:
                    #print("No its not a prime number")
                    break
            else:
                print(s,end=' ')
                    #print("Yes its a prime number")
            #else:
             #   print("No! ITs not a prime number")

print(p(1,50))
