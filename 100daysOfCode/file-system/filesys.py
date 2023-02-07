file = open("file.txt")

# file.write('I am writing content in file!!')

# file.write('\nNow I am tring to append the content inside the file !!')

s = file.read()
print(s)

file.close()




#below line will show error because the file is closed now
# file.write('x')