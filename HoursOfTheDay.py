hours = dict()
hoursList = list()
inp = input('Enter a file name: ')

#Create a handle to deal with files, guard it against errors
#try:
#    fhand = open(inp)
#except:
#    print('Could not oppen file: ', inp)
#    exit()

# DEBUG:
fhand = open('mbox-short.txt')
#Single out the useful lines
for line in fhand:
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    line = line.split()
#Find useful information
    time = line[5]
    hour = time[:2]
#Add useful info to the dictionary
    hours[hour] = hours.get(hour, 0) +1

#sort dictionary
#hours.items().sort()

for key, val in hours.items():
    #print(key, val)
    hoursList.append((key, val))
hoursList.sort()
for key, val in hoursList:
    print(key, val)
