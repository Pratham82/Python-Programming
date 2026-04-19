import datetime

time1 = datetime.time(5,25,1)

print(time1)

# retrieving various attributes
# Time instance holds values of timeand not the date.
print("Hour: ",time1.hour)
print("Minutes: ",time1.minute)
print("Seconds: ",time1.second)
print("Microseconds: ",time1.microsecond)
print("Timezone: ",time1.tzname())


# findind min max values
print(datetime.time.min)

print(datetime.time.max)

# resolution
print(datetime.time.resolution)

# Finding Date values
this_day = datetime.date.today()

print(this_day)

# Time tuple similar to named tuple
print("Time tuple: ",this_day.timetuple())

# Various attributes of date class
print("ctime: ",this_day.ctime())
print("toordinal: ",this_day.toordinal())
print("year: ",this_day.year)
print("month: ",this_day.month)
print("day: ",this_day.day) 

# min max dates
print(datetime.date.min) 
print(datetime.date.max) 
print(datetime.date.resolution) 

# replace method for modifying dates

date1 = datetime.date(2020,5,20)
print(date1)

# We can replace attributes by passing in replace method as arguments
date2 = date1.replace(day=21)
date2 = date1.replace(year=2021)
print(date2)

# Applying arithmetics on dates 
diff = date2 - date1 
print(diff)

d1 = datetime.date(1997, 8,9)
d2 = datetime.date(2020, 8,9)
print("age: ",(d2-d1))
