#TIME TO LEARN SOME PYTHON

# makes a comment (shotcut to comment selection -> cntl + E + C, undo cntrl + E + U)
# python is case-sensitive

#print syntax requires () in python 3, python 2 does not. Both requite quaotation marks for strings
print ("Hello world")
print (5)

#assigning variables
name = "Daniel"
number = 5

#arithmetic

#addition
x = 7
y = 2
sum = x + y
print(sum)

#subtraction
difference = x - y
print(difference)

#division

quotient = x / y
print(quotient)

#multiplication

product = x * y
print(product)

#floats and ints
# in python 2, a number with a decimal point is stored as a float, a non-decimal number is stored as an int
# in python 2, 7/2 would yeild a result of 3 as the data is truncated because both numbers are int.
# Adding a decimal to either/both numbers will return a float of 3.5
# python 3 automatically converts int and float data so that 7/2 equates to 3.5 regardless

# multiline strings are made with triple quotes
# if a multi-line string is not assigned to a variable, it acts like a multi-line comment
haiku = """The old pond,
A frog jumps in:
Plop!"""

print(haiku)

# booleans

name_is_Dan = True
age_is_1000 = False

# typecasting
# python automatically determines a data variable's type based on what is data assigned to it
# use int() to cast to int, str() to cast to string, float() to cast to float

int7 = 7
float7 = 7.
string7 = "7"

sum_7 = int7 + int(string7)
print(sum_7)



