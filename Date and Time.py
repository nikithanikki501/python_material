## Dates and Times
# To deal with dates and times we have seperate packages in Python - datetime
from datetime import date, datetime, timedelta  # Import specific classes from datetime module
import time  # Import time module for working with timestamps

# 1. Create a date object from an ISO-formatted string (YYYY-MM-DD)
date_obj = date.fromisoformat('2019-12-04')  # Converts string to a date object
print("Date from ISO string:", date_obj)  # Output: 2019-12-04

'''
Use fromisoformat():

When you're reading dates in ISO format

To write cleaner and safer code

Especially useful in data pipelines, logs, config files, or web APIs where ISO is the norm
'''

# 2. Replace components of a date (year, month, or day)
original_date = date(2002, 12, 31)  # Creates a date object: December 31, 2002
updated_date = original_date.replace(day = 26)  # Replaces the day with 26 (keeps same year and month)
print("Updated date:", updated_date)  # Output: 2002-12-26

# 3. Use timedelta to calculate a future date
now = datetime.now()  # Gets the current local date and time (e.g., 2025-04-30 20:15:00)
print("Current date-time:", now)  # Prints current date and time
future = now + timedelta(days = 730)  # Adds 730 days (approx. 2 years) to current datetime
print("Date-time after 2 years:", future)  # Prints future date-time after 2 years

# 4. Convert a datetime string to a datetime object and extract parts
date_time_str1 = '2027-03-25 07:54:47.904304'  # Define datetime string with microseconds
dt_obj1 = datetime.strptime(date_time_str1, '%Y-%m-%d %H:%M:%S.%f')  
# strptime() parses the string using specified format:
# %Y = 4-digit year, %m = 2-digit month, %d = day, %H:%M:%S = time (24-hr), %f = microseconds

print("Parsed Date:", dt_obj1.date())  # Extracts and prints just the date part
print("Parsed Time:", dt_obj1.time())  # Extracts and prints just the time part
print("Parsed Date-Time:", dt_obj1)    # Prints the full datetime object

# 5. Parse a datetime string with a different format and format it to a readable string
date_time_str2 = '2018-jan-02 08:15:27'  # Define another datetime string with abbreviated month
dt_obj2 = datetime.strptime(date_time_str2, '%Y-%b-%d %H:%M:%S')  
# %b = abbreviated month name like Jan, Feb, etc.
print(dt_obj2)

# Format the datetime object to a custom readable format using strftime
print("Formatted:", dt_obj2.strftime('%A, %B %d, %Y %I:%M %p'))  
# %A = full weekday name, %B = full month name, %d = day
# %Y = year, %I = hour (12-hour), %M = minutes, %p = AM/PM
# Example output: Tuesday, January 02, 2018 08:15 AM


"""##Date Formatting**

%a	Abbreviated weekday name.	Sun, Mon, ...

%A	Full weekday name.	Sunday, Monday, ...

%w	Weekday as a decimal number.	0, 1, ..., 6

%d	Day of the month as a zero-padded decimal.	01, 02, ..., 31

%-d	Day of the month as a decimal number.	1, 2, ..., 30

%b	Abbreviated month name.	Jan, Feb, ..., Dec

%B	Full month name.	January, February, ...

%m	Month as a zero-padded decimal number.	01, 02, ..., 12

%-m	Month as a decimal number.	1, 2, ..., 12

%y	Year without century as a zero-padded decimal number.	00, 01, ..., 99

%-y	Year without century as a decimal number.	0, 1, ..., 99

%Y	Year with century as a decimal number.	2013, 2019 etc.

%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23

%-H	Hour (24-hour clock) as a decimal number.	0, 1, ..., 23

%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12

%-I	Hour (12-hour clock) as a decimal number.	1, 2, ... 12

%p	Locale’s AM or PM.	AM, PM

%M	Minute as a zero-padded decimal number.	00, 01, ..., 59

%-M	Minute as a decimal number.	0, 1, ..., 59

%S	Second as a zero-padded decimal number.	00, 01, ..., 59

%-S	Second as a decimal number.	0, 1, ..., 59

%f	Microsecond as a decimal number, zero-padded on the left.	000000 - 999999

%z	UTC offset in the form +HHMM or -HHMM.	 

%Z	Time zone name.	 

%j	Day of the year as a zero-padded decimal number.	001, 002, ..., 366

%-j	Day of the year as a decimal number.	1, 2, ..., 366

%U	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, ..., 53

%W	Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, ..., 53

%c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013

%x	Locale’s appropriate date representation.	09/30/13

%X	Locale’s appropriate time representation.	07:06:05

%%	A literal '%' character.
"""