
# # slicing string in python
# a = "bipin"
# print(a[0:3]) # Here characteres starting from index 0 and ending at index 2 will be printed.
# # Here, index 3 in excluded.
# # i.e output >>>  bip << from 0 to 2.. index0, index1, index2 will be printed.
# #  First index is included , last index in excluded

# print(a[:3])
# #  putting 1st element blank is valid, by default python puts 0 
# print([0:])
# #  putting 2nd element black is also valid, by default python puts (last_index+1) i.e LENGTH of the string




# NEGATIVE index
# a = "bipin"
# index = b = 0 = -5
# index = i = 1 = -4
# index = p = 2 = -3
# index = i = 3 = -2
# index = n = 4 = -1


# Slicing with SKIP values


# a = name[1,3,With_the_skip_values_of]
# 3rd element = skip values



name = "haribadahur"
a = name[0:] # no character will be skipped#
a = name[:len(name)] # no character will be skiped



name = "haribadahur"
a = name[0:len(name):1] #no charater will be skiped
print(a)
a = name[0:len(name):2] #one character will be skipped
print(a)



# Illegal # VALUE ERROR
a = name[0:len(name):0] 
#Value error : slice step cannot be zero
print(a)