my_list = ['1', '2', '3', '4', 5, '6', '7']

# if else in python
# for x in my_list:
#     if(int(x) > 4):
#         print(x, 'is greater than 4')
#     elif(int(x) == 4):
#         print(x, ' is equal to 4')
#     else:
#         print(x, 'is less than 4')


# if 2 in my_list:
#     print('present')
# else:
#     print('not present')

# length in pyhton list

# print(len(my_list))
# print(my_list.index('5'))

# my_list.append('8')
# print(my_list)

# my_list.insert(1, '1.5')
# print(my_list)

# my_list.pop()
# print(my_list)

# my_list.remove('1.5')
# print(my_list)

# my_list = list()
# print(my_list)

# my_list.clear()
# print(my_list)

# my_list.reverse()
# print(my_list)

my_list = [1, 1, 0, 2, 3, 4, 7, 8, 3, 4, 2, 6, -7]
# my_list.sort()

# if we donot want to change an orginal list we use sorted function.
# my_new_list = sorted(my_list)
# print(my_new_list)

# print(my_list)


# SLICING
# last index is not included
# from index 4 to index less than 5
# a = my_list[4:5]
# # if we dont specify the start index it starts all the way from begining.
# a = my_list[:5]
# print(a)

# # starts all the way from the begining to the end with one STEP
# a = my_list[::1]
# print(a)

# # starts all the way from the begining to the end with two STEP
# a = my_list[::2]
# print(a)

# # nice trick to reverse our list
# a = my_list[::-1]
# print(a)


# coping a list

# list_fruits = ['apple', 'mango', 'bannana', 'pineapple']
# list_copy = list_fruits
# # here list_copy is a pointer,(both the list refers to the same list in the memory) so if we change anything in list copy list_fruits will be also changed.

# list_copy = list_fruits.copy()
# # doing this the orginal list will not be changed.

# list_copy = list(list_fruits)
# # list also makes actual copy to list.


# LIST COMPRIHENSING ADVANDED TECHNIQUE, ELEGENT AND FAST WAY TO  CREATE NEW LIST WITH EXISTING LIST.
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i*i for i in my_list]
print(b)
# here each element is squared
