min = None
max = None

while True :
    line = input('> ')
    if line == 'done':
        break

    else:
        number = int(line)
        if max == None or max < number:
            max = number

        if min == None or min > number:
            min = number

print('Maximum', max, 'Minimum', min)
