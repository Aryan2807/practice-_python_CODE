import pickle
stu={}
p=open('C:\\Users\\user\\Desktop\\coding\\personal\\File I O\\binary\\files\\student.dat',"wb+")
ans="y"
while ans=="y":
    rno= int(input("enter the roll number:\t"))
    name=input("enter the name:\t")
    subjects=int(input("Enter the no. of subjects"))
    stu[rno]=rno
    stu[name]=name
    stu[subjects]=subjects
    pickle.dump(stu,p)
    ans=input("want more records Y/N")
p.seek(0)
o=pickle.load(p)
print(o)