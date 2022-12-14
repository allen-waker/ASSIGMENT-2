c = [0,1,0,1,0,1,0]
c.sort()
print(c)


#without sorting
d = [1,20,30,50,5,2,7,3,4,6]
n = len(d)
for i in range(n):
    for j in range(i+1,n):
        if d[i]>d[j]:
            d[i],d[j]=d[j],d[i]
print(d)
