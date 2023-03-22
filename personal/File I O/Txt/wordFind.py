content=True
i=1
with open("exampleLOG.txt") as f:
    while content:
        content=f.readline()
        if ("available") in content:
            print(f"present {i}")
        i+=1
        