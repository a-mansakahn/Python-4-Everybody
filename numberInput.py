full = []
while True :
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    else:
        full.append(int(inp))

print('Minimum: ', min(full), '\nMaximum: ', max(full))
