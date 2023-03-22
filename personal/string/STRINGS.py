a="aryan"
print(a[0:3])

#skiping
b="aryanIsSavage"
print(b[0::3]) #last (3) is the skip value

#string function
story="once upon a time there was a teenager called Aryan. He begain his journey by finding his passion"
print(len(story))
print(story.endswith("passion"))
print(story.count("his"))
print(str.capitalize(story))
print(story.find("begain")) #-1 means not there
print(story.replace("Aryan", "Legendary Aryan"))
print(story.replace(".","\n"))

#ESCAPE SEQUENCE CHARACTER
'''\n--> new line
\t--> tab (more space)
\'--> single quote
\\ --> backslash'''