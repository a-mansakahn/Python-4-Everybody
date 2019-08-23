try :
    hoursPrompt = 'Enter hours worked: \n'
    hours = int(input(hoursPrompt))
    ratePrompt = 'Enter rate: \n'
    rate = int(input(ratePrompt))
    otHours = 0
    pay = 0

    if hours <= 40 :
        pay = hours * rate

    elif hours > 40 :
        otHours = hours - 40
        pay = rate * 40 + (otHours * rate * 1.5)

        print(pay)
except :
    print('Please enter an integer')
