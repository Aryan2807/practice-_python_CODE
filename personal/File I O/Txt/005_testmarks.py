ran=int(input("enter the total number of students:"""))
with open("marks.txt","w") as f:
    
    for i in range (ran):
        i=i+1
        l=[]
        print(f"enter the details of student {i}, below :-")
        roll=int(input("RollNo:\t"))
        name=(input("Name:\t"))
        Nosub=int(input("Enter the number of subject"))
        def subs():   
            for c in range (Nosub):
                subject=(input("Subject name:\t"))
                marks=int(input("Enter the marks:\t"))
            return
        k=(subs)
            
        r=(f"Name:{name} RollNo:{roll} {subs} ")
        l.append(r)
        s=str(l)
        f.write(s)
        f.write("\n")