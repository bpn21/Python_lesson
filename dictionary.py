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