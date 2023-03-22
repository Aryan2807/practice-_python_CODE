def percentage(num):
    return (sum(num)/b)*100
'''num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
num4=int(input("enter the fourth number"))
num5=int(input("enter the fifth number"))
b=int(input("enter the maximum num"))
a=num1,num2,num3,num4,num5
print(percentage(a))'''



i=0
while i<1000:
    i=i+1
    num=int(input("enter the "+str(i)+" number:\t" ))
    if num=="done":
        break
    b=int(input("Enter the maximum number:\t"))
    a=num
    print(percentage(a))