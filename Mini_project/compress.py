str1 = 'aaaaaassssssbbbbcccczzzz'
output = ''
char=str1[0]
count=0
for i in str1:
    if i == char:
        count+=1
    else:
        output = output+str(count)+char
        count=1
        char=i
output=output+str(count)+char
print(output)
