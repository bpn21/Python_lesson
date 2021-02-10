#Variables
# variables does not start with numbers
# variables can contain alphabets, digits and underscores
# variable can olny start with an alphabet and unserscores
# variables cannot start with digits.
# No white space is used inside a variable name


# theses all are literals
# a = "Bipin"
# a_21 = "Gaire"
# b = 12 
# c = 12.2
# d = True
# e = None


#  Python automatically identifies data for us

    #  a = 1  >>>   is automatically of class <int>
    #  b = "bipin"  is automatically of class <float>




#Keyboards>>>> reserved words
'''
def 
none
true
while
elif
return
try
class
'''



#Identifiers
'''
    Data Types in Python
    Integers
    Floating Point numbers
    Strings
    Boolens (Either true or false) 
  " boolen variable >>>>>> a = True "
    None
    
'''


#Printing the types of variables  
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# TO RUN PYTHON INTERPERATOR
# TYPE PYTHON AND HIT ENTER



# Common OPERATORS IN PYTHON

# 1) Arthematic OPERATORS +,-,/,etc
# 2) Assignment OPERATORS =,+,+=,-=,etc
# 3) Comparision OPERATORS ==,>,>=,<=,!=,etc
# a = (2>5)
# print("2>5 , the result is ", a)
# 4) Logical operators and, or ,not



# What is type casting?
# Way to convert one datatype to another datatype.
# a = "1234" # here, a is a string
# print(a+5) # this is not allowed


# if a = "123bipin"
# It shows an error >>> invalid literal for int

# BUT

# a = int(a) # Tries to convert string to integer. it only TRIES to convert.
# print(a+5) # This is valid , 

# A number can be converted into string and viseversa
# str(23)   >>"23"  integer to string conversion
# int("32") >>32 string to integer conversion
# float(12) >>12.0 interger to float converion
# type function is used to find the type of data variable in python




# Check the type of variable assigned using input function

# a = input("enter you name :")
# print(a)
# print(type(a)) # a is string

# a = input("enter your age :")
# print(a)
# print(type(a)) # a is also a string



# ADDITIONAL OF TWO NUMBERS

a = input("enter first number for addition")
b = input("enter second number for addition  ")
a = int(a)
b = int(b)
print("Additional of two numbers",(a+b)/2)

#Write a program to enter square of numbers inered by user 

a = input("enter a number")
a = int(a)
print("square of number",a*a)