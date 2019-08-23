import re
inp = input('Enter a regular expression: ')
count = 0
fhand = open('mbox.txt')
for line in fhand:
    if re.search(inp, line): count += 1
print('There are', count, 'matches for', inp, 'in mbox.txt.')
