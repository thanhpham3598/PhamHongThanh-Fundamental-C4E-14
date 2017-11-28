sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello, I'm Thanh and here are my sheep's sizes: ")
print(sizes)

print("Now my biggest sheep has size", max(sizes), "let's shear it!")
index = sizes.index(max(sizes))

sizes[index] = 8
print('After shearing, here is my flock:')
print(sizes)
month = int(input('Number of months: '))
for i in range(month):
    print('Month', i + 1, ':')

    sizes = [x + 50 for x in sizes]
    print("One month has passed, now here is my flock:")
    print(sizes)

    if i + 1 < month:

        print("Now my biggest sheep has size", max(sizes), "let's shear it!")
        index = sizes.index(max(sizes))

        sizes[index] = 8
        print('After shearing, here is my flock:')
        print(sizes)
print("My flock has size in total:", sum(sizes))
print("I would get", sum(sizes), '* 2$ =', sum(sizes)*2 )
