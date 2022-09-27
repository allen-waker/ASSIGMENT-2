
#write a program to get the factorial number of a given number

class program:

    def checkfactorial(self):
        f = 1
        for i in range(1,num+1):
            f*=1

        print("factorial = ",f)

obj = program
num = int(input("enter a number : "))
obj.checkfactorial(num)