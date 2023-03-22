myfile=open (r'E:\\poem.txt',"r")
str=""
size=0
tsize=0
while str1:
    str1=myfile.readline()
    tsize=tsize+len(str1)
    size=size+len(str1.strip())
print("size of the file after removing all EOL character and blank lines:",size)
print("the total size of the file:",tsize)
myfile.close()