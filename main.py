from beeprint import pp

try:
    10 * (1/0)
except ZeroDivisionError as err:
    print(err)

try:
    raise NameError('HiThere')
except NameError as err:
    print(err) #HiThere

