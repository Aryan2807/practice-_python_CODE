def max(num1,num2,num3,num4):
    if (num1>num2):
        if(num1>num3):
            if(num1>num4):
                return num1
            else:
                return num4
    elif (num2>num3):
        if (num2>num4):
            return num2
        else:
            return num4
    elif (num3>num2):
        if (num3>num4):
            return num3
        else:
            return num4
a=int(input("enter the first number:\t"))
b=int(input("enter the second number:\t"))
c=int(input("enter the third number:\t"))
d=int(input("enter the fourth number:\t"))
maximum=max(a,b,c,d)
print(maximum)