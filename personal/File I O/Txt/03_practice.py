from re import A


for i in range (1,11):
    with open(f"C:\\Users\\user\\Desktop\\coding\\school\\File I O\\_multiply_\\multiplication_table_of_{i}.txt", 'w') as a:
        for j in range (1,11):
            a.write(f"{i}X{j}={i*j}\n")