day = input("enter day: ")
month = input("enter month: ")
year = input("enter year: ")
if day != '':
    day = int(day)
else:
    day = 0
    print("invalid input")
if month != '':
    month = int(month)
else:
    month = 0
    print("invalid input")
if year != '':
    year = int(year)
else:
    year = 0
    print("invalid input")
if 1 <= day <= 31 and 1 <= month <= 12 and 1950 <= year <= 2020:
    if year % 100 < 10:
        print(f"{day}/{month}/0{year%100}")
    else:
        print(f"{day}/{month}/{year%100}")
else:
    print("invalid input")
