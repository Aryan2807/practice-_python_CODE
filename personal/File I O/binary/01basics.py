#pickling is a process to store a text content into binary file.
#unpickling is a process to convert a binary file  in a readable form.
#when we write in a file we use .dump()
#when we wanna read a file we use   .load()
import pickle
with open("C:\\downlaod.jpg","rb") as f:
    a=f.load()
    print(a)