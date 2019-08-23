count = dict()
inp = input('Enter file name: ')

try:
    fhand = open(inp)
except:
    print('Can not open file: ', inp)
    exit()
fhand = open('mbox-short.txt')
for line in fhand:

    words = line.split()

    for word in words:
        if words[0] != 'From': continue
        print(words[1])
        if words[1] not in count:
            count[words[1]] = 1
        else:
            count[words[1]] += 1
print(count)
