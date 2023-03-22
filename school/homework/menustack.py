from operator import truediv
from tkinter import Y


l=[]
b="yes"
while True:
    print(l)
    option=int(input("1:Pop\n2:Push\n:3:Peek\n4:Display:\n------->"" "))
    
    if option==1:
        l.pop()
    elif option==2:
        u=(input("required element to push:  "))
        l.append(u)
    elif option==3:
        index=len(l)-1
        print(l[index])
    elif option==4:
        print(l)