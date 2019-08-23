min = None
max = None
for number in [17, 1, 99, 22, 45, 10,] :
    if min == None or min > number :
        min = number

    if max == None or max < number :
        max = number

print('Maximum', max, 'Minimum', min)
