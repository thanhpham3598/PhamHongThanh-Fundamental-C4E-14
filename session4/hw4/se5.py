rabbits = [1, 2]
for i in range(5):
    if i > 1:
        rabbits.append(rabbits[i - 1] + rabbits[i - 2])
    print("Month {0}: {1} pair(s) of rabbit".format(i, rabbits[i]))
