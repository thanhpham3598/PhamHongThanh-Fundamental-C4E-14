# a
#
# n = int(input("Enter a number:"))
# for a in range(n):
#     print("*", end='')
#
#
# b
#
# n = int(input("Enter a number:"))
# for a in range(n):
#     if a % 2 == 0:
#         print("x", end='')
#     else:
#         print("*", end='')
#
#
# c
#
# a = int(input("Enter number of column:"))
# b = int(input("Enter number of row:"))
# for i in range(a*b):
#     if i % a == (a - 1):
#         print("x")
#     else:
#         print("x", end='')

# d

a = int(input("Enter number of column:"))
b = int(input("Enter number of row:"))
for i in range(b):
    if i % 2 == 0:
        for c in range(a):
            if c % 2 == 0:
                print("x", end='')
            else:
                print("*", end='')
    else:
        for c in range(a):
            if c % 2 == 0:
                print("*", end='')
            else:
                print("x", end='')
    print()
