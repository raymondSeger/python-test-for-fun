def increment_by(n):
    return lambda x: x + n

function1 = increment_by(10)
print( function1(0) ) #10
print( function1(15) ) #25