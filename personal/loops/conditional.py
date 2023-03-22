'''first=int(input("Enter first number"))
middle=int(input("Enter second number"))
if(first>middle):
    print("number",first,"is bigger than",middle)
elif(first==middle):
    print("number",middle,"is equal to",first)
else:
    print("number",middle,"is bigger than",first)'''


a=int(input("enter the number"))
b=int(input("enter 2nd number"))
c=(a+b)
print(c)
if(c%2==0):
    print("the product is an even number")
elif(c==0):
    print("none")
else:
    print("product is an odd number")