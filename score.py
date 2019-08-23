try :
    prompt = 'Please enter a score between 0.0 and 1.0: \n'
    imp = input(prompt)
    score = float(imp)
    if score < 0.0 or score > 1.0 :
        print('Bad Score')
    else :
        if score >= 0.9 :
            print('A')
        elif score >= 0.8 :
            print('B')
        elif score >= 0.7 :
            print('C')
        elif score >= 0.6 :
            print('D')
        else :
            print('F')


except :
    print('Please enter a number')
