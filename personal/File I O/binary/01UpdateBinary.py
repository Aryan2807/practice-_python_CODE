'''for postion of file pointer :-
  to get the address:      tell()
  to move your pointer:    seek()'''
p=open("C:\\Users\\user\\Desktop\\coding\\personal\\File I O\\binary\\files\\sample.txt","r")
print("default postiton is:",p.tell())
print('reading 3 byte:',p.read(3))
print("now the filw [ointer location is:",p.tell())

p.close()