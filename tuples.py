# Cannot update the values of tupple
#Tuple is the immutable data type in python >>> Cannot change
# immutable >> cannot change 
# mutable >> changes

# t=() >> empty tuple
# t=(1,) >> tuple with only one elements needs comma
# t=(1) THIS IS WRONG WAY TO DECLARE TUPLE, this is not a tuple, this is a number
# t=(1,7,2) >> tuple with more than one element

# Once defined a tuple cannot be altered or manipulated




# AS WE HAD METHODS FOR LISTS , WE HAVE METHODS FOR TUPLES TOO
t = (1,2,3,4,5,1)
print(t)
print(t.count(1))
print(t.index(1)) # returns the index of 1st occerance of 1 in tuple    