number = int(input('How many B bacterias are there? '))
mins = int(input('How much time in minutes will we wait? '))

time = mins // 2

result = number * 2 ** time

print('After {0} minutes, we would have {1} bacteria'.format(mins, result))
