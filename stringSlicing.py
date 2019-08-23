str = 'X-DSPAM-Confidence:0.8475'
begin = str.find('0') #the find argument must be written as a string
num = float(str[begin:])
print(num)
