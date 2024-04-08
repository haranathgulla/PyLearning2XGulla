# Home - Please complete
# Fact program with the function
# default = 1

# Reverse a String

# str = "Pramod"
# rev_str = ""
# for c in str:
#     rev_str = c+ rev_str
#
# print(rev_str)

# xyz = "Haranath"
# rev_xyz = ""
# for s in xyz:
#     rev_xyz = s+ rev_xyz
#
# print(rev_xyz)

# abc = "Sunithaa"
# r_abc = ""
# for d in abc:
#     r_abc = d+ r_abc
#
# print(r_abc)

# def rev_string(str):
#     rev_str = ""
#     for d in str:
#         rev_str = d + rev_str
#     return rev_str

# name = rev_string("Haranath")
# print(name)


#------------------------------------------------
def rev_string(str):
    rev_str = ""
    for d in str:
        rev_str = d + rev_str
    return rev_str

original_str = input("enter the string\n")
original_str = original_str.lower()
rev_str = rev_string(original_str)
print(rev_str)

#Palindrome - str = rev_str  ---> p
if original_str == rev_str:
    print("Palidrome")
else:
    print("It is not Palidrome")



