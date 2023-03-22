n=int(input("number of winners:"+"\t"))
win={}
for i in range(n):
    a=input("Names of the winners: \t")
    b=int(input("Number of trophy won: \t"))
    win[a]=b
    
print("dictionary: \n")
print(win)
    