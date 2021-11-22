fp = open("tesString.txt" , 'r')

contents = fp.read()

contents = contents.split()

fp.close()

print(contents)
