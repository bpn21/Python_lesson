text = input("enter a text : ")
print(type(text))
length = len(text)
print("length of text : ",length)
count = 0
reverse = ['','','','','']
for i in range(length):
    reverse[count] = text[length-count-1]
    # array[count] = text[length-1]
    count = count + 1
    # length = length - 1

print(type(reverse))
print(reverse)