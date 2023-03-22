letter='<name>'
middle='''we are happy to inform you that we are ready to offer you a place
for backend development and we see you as a valiuable asset to our company
.As for the salary we can offer you $50/hr +10k bonus.
have a great day ahead!
thanks and regards \n
<senders name> \n
date'''
name=input("enter your name .\n")
date=input("enter the date: \n")
sendersname=input("enter senders name: \n")
letter=letter.replace("<name>",name)
middle=middle.replace("date",date)
middle=middle.replace("<senders name>",sendersname)
middle=middle.capitalize
print("\n")
print(letter)
print("\n")
print(middle)
