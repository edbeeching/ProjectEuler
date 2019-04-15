#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:09:40 2019

@author: edward

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

days = 'mon tue wed thu fri sat sun'.split(' ')
months = 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')
durations = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

num_sundays = 0
weekday = 0 #  a monday

for year in range(1900, 2001):
    #print(year)
    if is_leap(year):
        #print('leap year', year)
        durations[1] = 29
    else:
        durations[1] = 28

    for ind, month in enumerate(durations):
        #print(months[ind], month)
        for indd, day in enumerate(range(month)):
            weekday += 1
            weekday = weekday % 7
            #print(days[weekday], indd)
            if year > 1900 and weekday == 6 and day==0:
                print('sunday', days[weekday], months[ind], year)
                num_sundays += 1


print(num_sundays)

