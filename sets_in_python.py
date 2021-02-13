# # Set is a collection of non repeatative elements.
# # This is example of set
# # s = {1,2,3,4}

# # IMPORTANT 
# # This will create empty dictionary not empty set.
# # s = {}
# # This is not empty set, this is empty dictionary.

# # EMPTY SET >>> s = set()
# # s = set()
# # print(type(s))


# # # Adding elem 





# # Can we add list to set ? 
# # >> ERROR >>Unhashable type 'list'
# # We cannot add list to set, because list is not hashable,
# # We can change the content of list. It is not hashable.
# # List can be changed so we cannot put list in set.
# # >>>>>>>>>>>>>>>s.(add[1,2,3])<<<<<<<ERROR<<<<<<<<<
# # s.add([1,2,3])    <<< ERROR : unhashable type list.

# # We can add tupple to set.
# # s.add((1,2,3))   
# # print(s)





# # Properties of set
# # Sets are unordered
# # sets are unindex
# # There is way to change itmes in set
# # sets cannot contain dublicate values.
# #
# # Consider the following set
s = {1,2,8,4}
# print(s)


# # s.remove(8)
# # print(s)
# # s.pop()
# # s.pop() # It removes the random value from set. jun pani hatauna sakcha
# # print(s)
# # s.clear() #It will make the set empty.
# # print(s)

a = {6,7,8,9}
s.union(a)
print(s)

# s.intersection({1,2,8,9})
# print(s)

