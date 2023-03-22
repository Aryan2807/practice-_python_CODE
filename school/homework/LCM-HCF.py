from re import I


def hcf(x,y):
    if x>y:
        small=y
    elif x==y:
        small=x,y
    else:
        small=x
    for i in range(1,small+1):
        if((x%i==0)and(y%i==0)):
            hf=i
    return hf


def lcm(o,p):
    if o>p:
        smalls=p
    elif o==p:
        smalls=o,p
    else:
        smalls=o
    a=0
    while (a==0):
        if(smalls%p==0)and(smalls%o==0):
            lc=smalls
            break
    return lc
omk=int(input("1: LCM \n 2: HCF "))
a=int(input("enter the number 1:\t"))
b=int(input("enter the number 2:\t"))
if (omk==1):
    print(lcm(a,b))
elif (omk==2):
    print(hcf(a,b))
else:
    print("invalid input")

