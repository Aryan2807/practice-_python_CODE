
    
limit=int(input("limit----: "))
for i in range(1,limit+1):
    for t in range(1,i):
        if(i%t==0):
            break
        else:
            print(i)
        
    
            
