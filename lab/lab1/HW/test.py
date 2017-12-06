from datetime import datetime
while True:
    time = datetime.now()
    hour = time.hour
    min = time.minute
    if hour == 21 and min == 33:
        print(hour)
        print(min)
        print(time)
        break
