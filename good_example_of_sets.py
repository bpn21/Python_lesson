
# Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names.Assume that there names are unique.
# Also for repetative keys and values in dictionary   



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


'''
Can the elements of following set be changed ?
s = { 8 ,  7  ,  ' guitar ' , [ 1 , 2 ] }
First thing list cannot be inside set. incase of tuple.
s = { 8 ,  7  ,  ' guitar ' , ( 1 , 2 ) }
Tuple ko value tw easai pani change hudainayo
'''