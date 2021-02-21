# Types of file 
# Text files (.txt,c,etc)
# binary files (.jpg,.dat,etc)
# python has lot of function for reading, updating and deleating files


# opening a file
 
# f = open("simple.txt","r")  # opens the file in read mode
# f = open("simple.txt")  # By default mode is read  # opens the file in read mode

# r >> mode for opening(read mode)
# open is builtin function in python
 
# data = f.read() # reads file content
# print(data) #
# f.close() #close the file




# data = f.readline() # reads file content
# data = f.readline() # reads file content
# data = f.readline() # reads file content
# data = f.readline() # reads file content


# 'r' >>> reading
# 'w' >>> wrinting
# 'a' >>> appending
# '+' >>> updating

# 'rb' >>> read in binary mode
# 'rt' >>> read in text mode



# Write Files in python

f = open('simple.txt','w')
f.write('please write.')
f.write('i am appending.')

f = open("simple.txt")
data = f.read()
print(data)
print(open("simple.txt").read())
if 'please' in data:
    print("'Please' is present")
else:
    print("'please' is not present")
f.close()