text = input("enter a text : ")
length = len(text)
count = 0
reverse = list()
for i in range(0,length):
    reverse.append(text[length-i-1])

list_to_string = ''.join(map(str,reverse))
print(list_to_string)


