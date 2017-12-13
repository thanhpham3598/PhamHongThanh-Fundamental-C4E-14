def is_inside(point, rec):
    if point[0] in range(rec[0], rec[0] + rec[2]) and point[1] in range(rec[1], rec[1] + rec[3]):
        return True
    else:
        return False

result = is_inside([100, 120], [140, 60, 100, 200])
print(result)
