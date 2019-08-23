finput = input('Please enter a filename: \n') #newline
try:
    fhand = open(finput)
except:
    print('Invalid filename, ', finput)
    exit()

for line in fhand:
    line = line.rstrip() #strip newline
    line = line.upper() #
    print(line)
