fhand = open('romeo.txt')
full = []
for line in fhand:
    #line = line.lower()
    words = line.split()
    for word in words:
        if word not in full: #Apparently 'not in' is a thing
            full.append(word)
        full.sort()
print(full)
