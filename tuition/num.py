num=int(input("Enter the number:"))
rev=0
nnum=num
while(nnum!=0):
    digit=nnum % 10;
    nnum=nnum//10
    rev=rev*10+digit
if rev==num:
    print(num, "is a palindrom number.")
else:
    print(num, "is not a palindrom number.")
