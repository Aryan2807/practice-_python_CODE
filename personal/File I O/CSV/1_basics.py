'''writerow function makes row wise list, '''
'''<eg> empdata=csv.writer(p)
 empdata.writerow(['name','roll','class'])'''
 
#code to understand more:==
import csv
with open('C:\\Users\\user\\Desktop\\coding\\personal\\File I O\\CSV\\smart.csv','w+') as a:
    dic=csv.writer(a)
    dic.writerow(['Sl.no','name','marks'])
    b=int(input("Number of Students"))
    for i in range (b):
        print(f"enter the data of student number {i+1}")
        oppai=int(input("Sl.no-\t"))
        thicc=input("name of the student--\t")
        thighs=int(input("marks--\t"))
        personality=[oppai,thicc,thighs]
        dic.writerow(personality)
    a.seek(0)
    m=a.read()
    print(m)    