# a = None
# if(a is None):
#     print('yes')
# else:
#     print('no')

# 'is' is used to check the value. == use garna ni huncha. but hamilai tha hunu parcha "is" ko kura ni.


# a = [45,56,8]
# # in identifies weather some_given_value is in the list or not
# print(345 in a) # returns true if there is 345 in list a.


# text = "bipin is a good boy"
text = "bi bipin pin"
text = " bi pin bi pin "

if("bipin" in text):
    print("this is bipin inside text")
else:
    print("this is no bipin inside text")

# if("bipin" is text):
#     print("This is bipin")
# elif("janak" is text):
#     print("This is Janak")
# elif("roshan" is text):
#     print("This is Roshan")

# else:
#     print("This sombody else")



# Spam detector

# text  = input("enter a text : ")

# if("hello" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("this is spam")
# else:
#     print('This is not a spam')

text = "hello"
text = "bipin"
# array = list(text)
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
