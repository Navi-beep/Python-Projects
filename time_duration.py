#Readable Time Durations
#Given a string input seconds, return a readable string of time featuring years, days, hours, minutes, and seconds.

#Example:
#Input: "31600000"
#Output:  "1 year, 0 days, 17 hours, 46 minutes, and 40 seconds"
#Note: Correct pluralization matters (1 year not 1 years)

def duration(s):
    minutes = s//60
    seconds = minutes*60
    hours = minutes//60
    days = hours//24
    year = days //365.25
    return f"That time is:{year} years, {days} days, {hours} hours, and {minutes} minutes, {seconds} seconds."

print(duration(60000))

import time 

seconds = time.time()
years = seconds/60/60/24/365.25
print(years)

#return none, have to fix
def stuff(seconds):
    seconds = time.time()
    years = seconds/60/60/24/365.25
    print(years)
    print('cats')

print(stuff(600000))


