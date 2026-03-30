src = open("raj.txt","r")
data = src.read()
src.close()

dst = open("atmiya.txt","w")
dst.write(data)
dst.close()
printf("file copied successfully.")