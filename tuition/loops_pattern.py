'''for i in range (5):
    for j in range (i):
        print(i)
        print('\n')
    '''
'''n=6
a=0
s=0
for i in range (a,n,1):
    for j in range (1,s+1):
        print(end="")
    for j in range (1,i+1):
        print(j,end="")
print()
'''
n=5
s=n*2-1
for i in range(1,n+1):
    for j in range(0,s):
        print(end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    s=s-2
    print()
