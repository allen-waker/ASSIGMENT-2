# Write a Python program to count occurrences of a substring in a string.

str1 = 'python is a pouplar language.'
print()
print(str1.count("popular"))
print()

#Write a Python program to count the occurrences of each word in a given sentence

string = " pyhton is a popular language."
word ="python"
list=[]
wordcount=0
list=string.split(" ")
for i in range(0,len(list)):
    if(word==list[i]):
        wordcount=wordcount+1
print("number of occurrences found in the string:")
print(wordcount)

#Write a Python program to get a single string from two given strings,separated by a space and swap
#  the first two characters of each string.
def chars_mix_up(a,b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a +' ' + new_b
print(chars_mix_up('abc','xyz'))

   

