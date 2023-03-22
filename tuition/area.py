a=(int(input("\t MENU: \n PRESS 1 FOR Ar.SQUARE \n PRESS 2 FOR Ar.RECTANGLE \n PRESS 3 FOR Ar.Circle \n PRESS 4 FOR Factorial \n")))

if a==1:
    b=(int(input("Enter the lenght of the square")))
    print(b**2)
elif a==2:
    c=(int(input("Enter the length of the rectangle: \t")))
    d=(int(input("Enter the breath: \t")))
    print(c*d)
elif a==3:
    e=(int(input("Enter the radius of the square: \t")))
    print(22/7*e**2)
elif a==4:
    f=(int(input("Enter the number for its Factorial")))
    factorial=1
    for i in range(1,f):
        factorial=factorial*i
        print(factorial*f)