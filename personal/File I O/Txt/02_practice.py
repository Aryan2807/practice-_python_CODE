myfile=open(r'E:\poem.txt',"r")
str=""
size=0
tsize=0
while str:
    str=myfile.readline()
    tsize=tsize+len(str)
    size=size+len(str.strip())
print("size of the file after removing all EOL character and blank lines:",size)
print("the total size of the file:",tsize)
myfile.close()