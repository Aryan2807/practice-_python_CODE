a=5
b=0 
try:
    print(a/b)
except Exception:
    print("anything with 0 is not divisible")
finally:
    print("I am always executed no matter what!")