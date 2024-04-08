# Task - Fibonacci series and Factorial
#
# # Factorial
#
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24
import math

# n = int(input("enter number:"))
# # print(math.factorial(n))
# if n < 0:
#     print("Fact")
# elif n == 0:
#     print("Fact - ",1)
# else:
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
# print("Fact ->>", fact)
#
# #Fibonaci series
#
# # 0,0+1, 0+1+1,
#
# # n = 7
#
# # 0, 1, 2, 3, 5, 8, 13

a , b = 0 , 1
while a < 10:
    print(a, end=" ")
    a, b = b, a+b