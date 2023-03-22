with open("okayyy.txt","r")as f:
    b=0
    a=f.readline()
    for i in a:
        if a=="india"or a=="bharat":
            b=b+1
    print(b)