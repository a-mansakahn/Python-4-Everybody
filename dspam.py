count= 0
total= 0
finput = input('Enter file name: ')
try:
    fhand = open(finput)
except:
    print('Invalid file name: ' , finput)
    exit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:') == False: #skips lines that dont start with ...
        continue
    colon = line.find(':')
    num = float(line[colon+2:]) #splice out the number
    total += num
    count += 1

print('Average spam confidence', total / count )
