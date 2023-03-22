'''rno=[]
mks=[]
for a in range(4):
    r,m=eval(input("Enter the no.,Marks:\t"))
    rno.append(r)
    mks.append(m)
d={rno[0]:mks[0],rno[1]:mks[1],rno[2]:mks[2],rno[3]:mks[3]}
print("Created dicktionary")
prin'''

n1=int(input("enter first number"))
n2=int(input("enter second number"))
product=0
count=n1
while count > 0:
    count=count-1
    product=product+n2
print("the product of",n1,"and",n2,"is",product)