count = dict()
#inp = input('Enter file name: ')
min = None
max = 0
#try:
#    fhand = open(inp)
#except:
#    print('Can not open file: ', inp)
#    exit()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.split()
    for words in line:
        if line[0] != 'From':continue
        count[line[1]] = count.get(line[1],0) + 1
for key in count:
    if min is None or min > count[key]:
        min = count[key]
    if max < count[key]:
        max = count[key]
print('Maximum: ', list(count.keys())[list(count.values()).index(max)], ' ',
max, '\nMinimum: ', list(count.keys())[list(count.values()).index(min)], ' ',
min)
