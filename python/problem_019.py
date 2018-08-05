#!/usr/bin/python
# Counting Sundays
# https://projecteuler.net/problem=19
#   1 Jan 1900 was a Monday.
#   Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
#   A leap year occurs on any year evenly divisible by 4,
#   but not on a century unless it is divisible by 400.
#
#   How many Sundays fell on the first of the month during the 
#   twentieth century (1 Jan 1901 to 31 Dec 2000)?

import time

# Function to create list of days of the year which are also beginning of 
# months.

def find_dates():
  DATES = []
  MONTHS = 0
  DAYS = 0
  YEAR = 1900
  while MONTHS < 1211:
    if (MONTHS % 12) in {0,2,4,6,7,9,11}:
     DAYS += 31
     DATES.append(DAYS)
    elif (MONTHS % 12) in {3,5,8,10}:
      DAYS += 30
      DATES.append(DAYS)
    elif (MONTHS % 12) == 1 :
      DAYS += 28
      DATES.append(DAYS)
    elif (((YEAR + (MONTHS / 12)) % 400 == 0) and (MONTHS % 12) == 1 ) or \
      ((YEAR + (MONTHS / 12)) % 4 == 0 and (YEAR + (MONTHS / 12) % 100 != 0) \
       and (MONTHS % 12) == 1 ):
      DAYS += 29
      DATES.append(DAYS)
    MONTHS += 1
  return DATES

start = time.time()

DATES=find_dates()[11:]
# After finding the number of days from 01/01/1900 that each month starts on
# we can iterate through them to find which are sundays by doing the below
SUNDAYS = 0
for start_of_month in DATES :
  if (start_of_month % 7) == 6:
    SUNDAYS += 1
result = SUNDAYS
elapsed = time.time() - start
 
print("Result %s found in %s seconds" % (result, elapsed))
