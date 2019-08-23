inp = input('Enter a file name: ')
fhand = open(inp)
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From': continue
    print(words[1])
    count += 1
print('There are ', count, 'lines in the file with From as the first word')
