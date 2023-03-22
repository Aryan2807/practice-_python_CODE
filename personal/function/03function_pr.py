#inches to cm ,,,, in*2.54
'''def conv_inchtocm (n):
    return (n)*2.54
a=int(input("enter the inches value"))
print(conv_inchtocm(a))'''


#####################
#.strip() removes unnessacery spaces in a string

def removenstrip(string,word):
    str=string.replace(word,"")
    return str.strip()
string=("MY NAME IS ARYAN")
a=input("Enter the desired word to remove:\t")
if (a=="MY" or "NAME" or "IS" or "ARYAN") :
    print(removenstrip(string,a))
else:
    print("User desired word is not available")