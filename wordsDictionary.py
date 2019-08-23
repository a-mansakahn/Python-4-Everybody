fhand = open('words.txt')
wordy = dict()
count = 0
for line in fhand :
    words = line.split()
    for word in words :
        wordy[word] = count
        count += 1
#print(words)
#print(words[count])
#print(wordy)
print('laptops' in wordy)
