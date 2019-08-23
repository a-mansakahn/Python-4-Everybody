count = dict()
#inp = input('Enter a file name: ')
#try:
    #fhand = open(inp)
#except:
    #print('Can not find file ', inp)
    #exit()
fhand = open('mbox-short.txt')
for line in fhand :
    words = line.split()
    for word in words :
        if words[0] != 'From' : continue #Had this in the upper loop and had an error
        if words[2] not in count:
            count[words[2]] = 1
        else:
            count[words[2]] += 1
print(count)
