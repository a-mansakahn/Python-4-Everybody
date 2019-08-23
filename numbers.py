import re
total = 0
count = 0
#variables
#file input
#inp = input('Enter file: ')
#try:
    #fhand = open(inp)
#except:
    #print('Can nott find file,' inp)
    #exit()
# DEBUG:
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    lst = re.findall('^New Revision: ([0-9.]*)', line)

    if len(lst) > 0:
        #print(float(lst[0]))
        total = total + int(lst[0])
        count += 1



#for var in lst:

avg = total / count
print(avg)
