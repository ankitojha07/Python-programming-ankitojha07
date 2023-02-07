import _datetime

x = _datetime.datetime.now()

print(x.month)
print(x.year)

print(x.strftime("%A")) # week day
print(x.strftime("%a")) # week day (half name)

print(x.strftime("%B")) # month
print(x.strftime("%b")) # month (half)

print(x.strftime("%c")) # fill day and date

print(x.strftime("%d")) # date

print(x.strftime("%F")) # Current date 

print(x.strftime("%g")) # last two letter of year

print(x.strftime("%h")) # date

print(x.strftime("%l")) # time in hours

print(x.strftime("%m")) # months number

print(x.strftime("%r")) # full time

print(x.strftime("%x")) # full date in mm/dd/yy

print(x.strftime("%y")) # year in yy

print(x.strftime("%p")) # AM PM
print(x.strftime("%P")) # AM PM (lowercase)






