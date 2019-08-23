count = dict()
#inp = input('Enter file name: ')
#try:
#    fhand = open(inp)
#except:
#    print('Can not open  file: ', inp)
#    exit()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.split()
    for words in line:
        if line[0] != 'From':continue
        words = line[1]
        at = words.find('@')
        domain = words[at+1:]
        count[domain] = count.get(domain,0)+1
print(count)
