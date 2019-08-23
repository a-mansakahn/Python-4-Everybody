def payot(hours, rate) :
    
    if hours <= 40 :
            pay = hours * rate
    else :
            ot = hours - 40
            pay = (rate * 40) + (ot * rate * 1.5)

    return pay

try :
    hours = int(input("Please enter hours worked: "))
    rate = int(input("Please enter pay rate: "))
    print(payot(hours, rate))

except :
    print("Please enter integers.")
