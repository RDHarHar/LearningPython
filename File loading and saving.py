# File loading and saving


# reading a file
try:
    my_file=open("test1.txt","r")
    print(my_file.read())

    #~~~~~

    #for line in test_file:
    #    print(line)

    #~~~~~

    my_file.readlines()

    #~~~~~
    
    my_file.close()

except IOError:
    print("Error 404: File not found or path is incorrect")
finally:
    print("exit")