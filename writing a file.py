# Writing to a file

#~~~~~

#new_file=open("newfile.txt",mode="w",encoding="utf-8")
#new_file.write("Writing to a new file\n")
#new_file.write("Writing to a new file\n")
#new_file.write("Writing to a new file\n")
#new_file.close()

#~~~~~

#fruit = ["Orange\n", "Apple\n", "Banana\n"]
#new_file=open("newfile.txt",mode="a+",encoding="utf-8")
#new_file.writelines(fruit)
#for line in new_file:
#    print(line)
#new_file.close()

#~~~~~

#cars=["Audi\n","Bentley\n","Toyota\n"]
#new_file=open("newfile.txt",mode="a+",encoding="utf-8")
#for car in cars:
#    new_file.write(car)
#print("Tell the byte at which the file cursor is:",new_file.tell())
#new_file.seek(0)
#for line in new_file:
#    print(line)
#
#    new_file.seek(4,0)
#print(new_file.readline())
#new_file.close()

#~~~~~

file=open("test1.txt","r")
for index in range(5):
    line=next(file)
    print(line)
file.close()