# Given an integer, float, and boolean, convert each to a string and concatenate them into a single string

a = 45
b = 45.
c = True

print("the first variable is of ",type(a))
print("the seconde variable is of ",type(b))
print("the third variable is of ",type(c),'\n')

d = str(a) + str(b) + str(c)
# str function converts any type of variable into string variable

print("after converting and cocantenate each variable ",d)
print(type(d))