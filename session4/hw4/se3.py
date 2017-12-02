x = int(input("Enter a number:"))
found = False
if x <= 0:
    print(x, "is not a prime number")
else:
    for i in range(2, x):
        if x % i == 0:
            print(x, "is not a prime number")
            found = True
            break
if not found:
    print(x, 'is a prime number')
