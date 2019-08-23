
count = 0
total = 0
average = 0
num = None
while True :
    inp = input('Enter a number: ')
    try :
        if inp == 'done' :
            break

        else :
            num = int(inp)
            count += 1
            total += num

    except :
        print('Invalid input')

print('Count: ', count, 'Total: ', total, 'Average: ', total / count)
