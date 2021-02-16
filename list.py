# # Python list are containers to store a set of values of any datatype.s
# friends = ['Apple','Aakash','Roshan',7,False]
# # friends[0] = 'Mango'
# # print(friends)


# # List slicing
# print(friends[0:5])
# print(friends[-3:])
# # pach (5) ota ma eauta matra print huncha. teo chai starting index ko hai.


# # Slicing with skip
# print(friends[0:5:5])

# Methods
numbers = [10,9,8,7,6,5,4,3,1,2,1]
# print(numbers.count(1)) #numbers of 1 in the list
# numbers[10]  #ERROR List index out of range


# numbers.sort()          #sorts the list
# numbers.reverse()       #reverses the list
# numbers.append(8)  # adds 8 at END of the list
# # APPEND ? >>GENERAL MEANING <<<>>> ADD at the end of doucment
# numbers.insert(3,'bipin') # adds bipin at index 3 , index of 3 will be 3
# numbers.pop(2) #Deletes the elements which is at index 2
# numbers.remove(21) #Deletes 21 from the numbers



# Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names.Assume that there names are unique.
s = set()
dict = {}
lan_list = []
name = ['a','b','c','d']
fav_language = ['a','b','c','d']
for i in range(4):
    name[i] = input("enter name of a person : ")
    # s.add(name[i])
    lan_list.append(name[i])
print(name)

# converting sets in to list
# my_list = list(s)

my_list = lan_list
for i in range(4):
    fav_language[i] = input("enter fav Language of "+ lan_list[i]+" :")
print(s)
for i in range(4):
    dict[name[i]] = fav_language[i]

print(dict)