# Dictionary is a collection of key-values pairs.
# Syntax :
car = {
    "tesla":"this is Electric car",
    "honda": "this is a fuel car",
    "tesla_model": ['s','3','x','y'],
    "honda_model": ['city',"jazz","civic"],
    "type":{
        "electric":"electric cars",
        "petrol":"petrol cars",
        "desel":"desel cars"
    }
}

# print(car.get('tesla'))
# print(car['tesla'])
# print(car['tesla_model'])
# print(car['honda_model'])
# print(car['type']['petrol'])


# Properties of Dictonry
# It is MUTABLE
# print(car['honda'])
# car['honda'] = "these are honda car"
# print(car['honda'])


# Dictionary are unorderd unline list
# Cannot contain dublicate keys

# Dictionary Methods
car = {
    "tesla":"this is Electric car",
    "honda": "this is a fuel car",
    "tesla_model": ['s','3','x','y'],
    "honda_model": ['city',"jazz","civic"],
    "type":{
        "electric":"electric cars",
        "petrol":"petrol cars",
        "desel":"desel cars"
    }
}

color = {
    "color":{
        "black":"this is black car",
        "white":"This is white car",
        "red":"This is red car"
    }
    }
# print(car.keys())
# print(car.values())
car.update(color)

# To add key values pair in dictionary in  use old_dictionary.update(new_dictionary_name)
# print(type(car.items()))

# print(car.get('printer'))
#This will return none or it doest not return error if there is no printer as key in dictionary


# print(car['printer'])
# This will send key error in Dictionary if there is no printer as key in the dictionary

# print(car.items())


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

# Dictionary ma keys same tw hudaina. so keys ko values list ma bhanda set ma add garda ramro.

my_list = lan_list
for i in range(4):
    fav_language[i] = input("enter fav Language of "+ lan_list[i]+" :")
print(s)
for i in range(4):
    dict[name[i]] = fav_language[i]

print(dict)