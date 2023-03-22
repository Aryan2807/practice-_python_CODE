ran=int(input("enter the total number of students:"""))
with open("marks.txt","w") as f:
    
    for i in range (ran):
        i=i+1
        l=[]
        print(f"enter the details of student {i}, below :-")
        roll=int(input("RollNo:\t"))
        name=(input("Name:\t"))
        Nosub=int(input("Enter the number of subject"))
        k=[]
        for c in range (Nosub):
            c=c+1
            sub=input("subject name:\t")
            marks=int(input(f"enter the {sub} marks :"" "))
            lol=(f"{sub}:{marks}")
            k.append(lol)
        p=str(k)
            
        r=(f"Name:{name} RollNo:{roll} {p} ")
        l.append(r)
        s=str(l)
        f.write(s)
        f.write("\n")