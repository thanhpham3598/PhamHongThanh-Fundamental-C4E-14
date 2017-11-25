h = int(input("Your height in cm:"))
w = int(input("Your weight in kg:"))
m = h / 100
b = w / (m * m)
if b < 16:
    print("You are severely underweight!!!")
elif b < 18.5:
    print("You are underweight!")
elif b < 25:
    print("You are normal. Keep fit!")
elif b < 30:
    print("You are overweight! Be careful!")
else:
    print('You are obese!!!!')
