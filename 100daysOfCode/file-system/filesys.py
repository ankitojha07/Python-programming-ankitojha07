# file = open("file.txt")

# file.write('I am writing content in file!!')

# file.write('\nNow I am tring to append the content inside the file !!')

# s = file.read()
# print(s)

# file.close()




#below line will show error because the file is closed now
# file.write('x')


s = "Hey there I am a programmer"

with open("test.txt","w") as f :
    f.write(s)
    f.close()


with open("test.txt","r") as f :
    r = f.read()
    print(r)