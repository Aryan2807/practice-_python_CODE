n=int(input("Enter the length of the pattern:\t"))

def pattern(n):
    for f in range (n):
        print((n-f)*"*")
        if n==1:
            print("*"*(f+n))
            if (n==f):
                break
    return

print(pattern(n))
