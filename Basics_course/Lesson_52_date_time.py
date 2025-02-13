
import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()


if target_datetime < current_datetime:
    print("Traget date has passed")
else:
    print("Traget date has not passed")

print(date)
print(today)
print(time)
print(now)
