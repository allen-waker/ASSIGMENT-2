#2list combain  4 types 

a = ["kapadiya","parmar","patel"]
b = ["karan","rahul","montu"]
c = [a[0],b[0],a[1],b[1],a[2],b[2]]
c =''.join(c)
print(c)




a = ["kapadiya","parmar","patel"]
b = ["karan","rahul","montu"]
for c in a+b: 
    c = a[0],b[0],a[1],b[1],a[2],b[2]
    c =' '.join(c)
print(c)



a = ["kapadiya","parmar","patel"]
b = ["karan","rahul","montu"]
for i,j in zip(a,b):
    print(i+j,end="") 




print()
a = ["kapadiya","parmar","patel"]
b = ["karan","rahul","montu"]
[print(i+j,end=' ') for i,j in zip(a,b)]


l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))