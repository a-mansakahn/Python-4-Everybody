domain = dict()
l = list()
inp = input('Enter a file name: ')

#Filename error catching, create a handle to deal with the file.
try:
    fhand = open(inp)
except:
    print('Could not open file: ', inp)
    exit()

#Iterate through lines of the file
for line in fhand:
    if not line.startswith('From:'): continue

#Turn strings into lists
    words = line.split()

#Identify the sender address
    word = words[1]

#Add sender address to the dictionary, adjust the value, update variable, repeat
    domain[word] = domain.get(word, 0) + 1

#Sort data by value, reveal top sender
for key, val in domain.items():
    l.append((val, key))
l.sort(reverse=True)
for val, key in l[:1]:
    print(key, val)

#Remember the colon after the from in 'line.startswith('From:')'
