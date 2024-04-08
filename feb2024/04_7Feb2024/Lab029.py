# String Concat
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)

name = "Hari"
age = 37
# r = name + age # TypeError: can only concatenate str (not "int") to str
r = name + str(age)  # Hari37
print(r)

g = "Hello"
# g += "world"
g = g + "World"
print(g)

# Increment and Decrement ++ , --
x = 5
x -= 1
print(x)
