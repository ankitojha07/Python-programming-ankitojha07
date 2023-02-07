import _datetime

x = _datetime.datetime.now()

print(x.month)
print(x.year)

print(x.strftime("%B")) # month
print(x.strftime("%A")) # week day