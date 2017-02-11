days=int(input("Enter the number of days"))
year=days/360
flag=days%360
month=flag/30
days=flag%30
print("The days in form of year,month and days is:",year,month,days)
