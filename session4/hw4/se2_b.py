nums = [1, 6, 8, 1, 2, 1, 5, 6]
x = int(input("Enter a number:"))
count = 0
for i in range(len(nums)):
    if x == nums[i]:
        count += 1

print("{0} appears {1} times in my list".format(x, count))
