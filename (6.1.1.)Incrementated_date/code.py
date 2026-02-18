day = int(input())
month = int(input())
year = int(input())
valid = True
max_days= 0
if year <= 0 or month == 0 or month > 12:
	valid = False
if month in [1,3,5,7,8,10,12]:
	max_days = 31
elif month in [4,6,7,9,11]:
	max_days= 30
else:
	if (year % 4 ==0):
		max_days = 29
	else:
		max_days = 28
if day > max_days or day < 1:
	valid = False 
day = day + 1
if day > max_days:
	day = 1
	month = month +1
if month > 12:
	month = 1
	year = year + 1
if valid:
	print(f"{day:02d}-{month:02d}-{year:04d}")
else:
	print("Invalid Date")
