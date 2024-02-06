#Strings
#bunch of charters
#"" or ''

# name1="Hari"
# name2='Hari'
# print(name1)
# print(name2)
#
# print(type(name1)) #Str
# print(type(name2))

# dir="C://abc.txt"
# print(dir)
# dir='C://abc.txt'
# print(dir)

# dir="C:\abc\abc.txt"
# print(dir)            #C:bcbc.txt #Here \a has a different meaning

# dir="C:\\abc\\abc.txt"
# print(dir)            #C:\abc\abc.txt

# dir = "C:\somedir\somedir"
# print(dir)              #C:\somedir\somedir

# dir = 'C:\somedir\some dir'
# print(dir)              #C:\somedir\some dir

# dir = 'C:\nsomedir\some dir'
# print(dir)              #C:
#                         #somedir\some dir # Here \n will make new line

# dir = r'C:\nsomedir\some dir'
# print(dir)              #C:\nsomedir\some dir # Here we use 'r' to make it raw string

#format string f
# s = "Amit"
# last_name="mishra"
# print("Your name is {s} {last_name}")  # Your name is {s} {last_name}
# print(f"Your name is {s} {last_name}")  # Your name is Amit mishra

s = "Amit"
last_name="mishra"
age=34
isMarried=False
print(f'Your name is {s} {last_name},your age is {age}, Are you {isMarried}') #Your name is Amit mishra,your age is 34, Are you False

