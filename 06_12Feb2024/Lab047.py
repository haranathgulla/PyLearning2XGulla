#Continue
# for num in range(1,10):
#     if num > 1:
#         print(num)

for num in range(1,10):
    if num % 2 ==0:  # even numbers
        print(f"Found even num {num}")
        continue
    else:
        print(f" odd num {num}")