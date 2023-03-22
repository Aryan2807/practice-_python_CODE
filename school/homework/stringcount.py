string=input("Enter the string:\t")
def counter(a):
    upper=lower=vowel=consonant=0

    for i in  string:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
         vowel=vowel+1
        else:
            consonant=consonant+1
        if i.islower():
            lower=lower+1
        if i.isupper():
            upper=upper+1
    print("Total number of vowel:",vowel)
    print("Total number of consonent:",consonant)
    print("Total number of uppercase letter:",upper)
    print("Total number of lowercase letter:",lower)
    return

print(counter(string))