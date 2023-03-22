with open("okayyy.txt") as f:
    content= f.read()
    with open("okayyy.txt","w") as f:
        content=content.replace("his","her")
        f.write(content)
