finput = input('Enter the file name: ')
if finput == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - you've been punk'd")
    exit()
else:
    try:
        fhandle = open(finput)
    except:
        print('File can not be opened: ', finput)
        exit()
count = 0 # none does not work with int types
for line in fhandle: #I'm not sure if this is technically all a part of the the else block
    if line.startswith('Subject'):
        count += 1

print('There were ', count, 'subject lines in ', finput)
