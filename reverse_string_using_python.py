text = input("enter a text : ")
length = len(text)
count = 0
reverse = list()
for i in range(length):
    reverse.append(text[length-count-1])
    count = count + 1

print(reverse)