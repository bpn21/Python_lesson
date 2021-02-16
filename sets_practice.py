# Write a program to create a dictionary of nepali word with values in english trasnlation.Provide user with an option to look it up.


dict = {
    "namaste" : "Hello",
    "ama": "mother",
    "buwa": "dad",
    "dai" : "younger brother",
    "bhae" : "elder brother",
    "gadi" : "vehicle"
}

print("The meaning of namaste is",dict['namaste'])
# print("The meaning of namaste is",dict['ansdjkansjn']) # gives an error
print("The meaning of namaste is",dict.get('kasdkj')) # Does not give an error, gives none insted 


# print(dict['gadi'])


# Write a program to input eight numbers from user and display all the unique numbers once
# s = set()
# for i in range(7):
#    num = (int(input("enter a number")))
#    s.add(num)
# print(s)


# Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names.Assume that there names are unique.
s = set()
dict = {}

name = ['a','b','c','d']
fav_language = ['a','b','c','d']
for i in range(4):
    name[i] = input("enter name of a person : ")
    s.add(name[i])
print(name)
my_list = list(s)

count = 0
for i in s:
    count = count + 1

print(count)

for i in range(count):
    fav_language[i] = input("enter fav Language of " + my_list[i]+" :")
print(s)
for i in range(count):
    dict[name[i]] = fav_language[i]

print(dict)