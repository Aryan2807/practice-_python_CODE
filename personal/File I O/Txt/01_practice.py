import os 
f=open(r'E:\\okay.txt','r')
t=f.read()
if "oh" in t:
    print ("oh is present in")
else:
    print("oh is not present in ")
f.close()       