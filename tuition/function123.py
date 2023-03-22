'''
def CI(a,b,c,d,e):
    s=a(1+b/c)**(d*e)
    return s
p=float(input("enter the initial principle number:\t"))
interest_rate=float(input("enter the intrest rate:\t"))
time_period=float(input("enter the time period per year:\t"))
time=float(time_period)
time_passed=float(int("enter the time passes:\t"))
CI1=CI(p,interest_rate,time_period,time,time_passed)
print("CI=",CI1)'''

'''def interest(principal,time=2,rate=0.10):
    return principal*rate*time
prin=float(input("enter the principle amount:"))
print("simple intrest with default ROI and time values is :")
sil=interest(prin)
print("rs.",sil )
roi=float(input('enter rate of interest'))
time=int(input("enter the time in years:"))
print("simple interest wth your provded ROI and the time values is :")
si2=interest(prin,time,roi/100)
print("Rs",si2)'''


def arcCalc(x,y):
    return x+y,x-y,x*y,x/y,x%y
num1=int(input("enter number 1:"))
num2=int(input("enter the number 2:"))
add,sub,multi,div,mod=arcCalc(num1,num2)
print("Sum of given numbers:",add)
print("substraction of given nmbers:",sub)
print("product of given numbers",multi)
print("Division of given numbers,",div)
print("modulo of given numbers:",mod)
