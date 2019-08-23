hours = int(input('Enter hours: '))
rate = int(input('Enter rate: \n' ))
pay = 0
ot = 0

if hours <= 40 :
    pay = hours * rate
else :
    ot = hours - 40
    pay = (rate * 40) + (ot * rate * 1.5)

print(pay)
