text = input("enter a text : ")
length = len(text)
print(length)
count = 0
reverse = list()
for i in range(0,length):
    reverse.append(text[length-i-1])
    print(reverse,"loop",i,",length-",i,"-1 = ",length-i-1)
list_to_string = ''.join(map(str,reverse))
print(list_to_string)


