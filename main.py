from beeprint import pp

try:
    10 * (1/0)
except ZeroDivisionError as err:
    print(err)