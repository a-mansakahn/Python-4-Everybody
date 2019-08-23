def letterGrade(x) :
    #Any other order and it won't work.
    if x < 0.0 or x > 1.0:
        return "Bad Score"
    elif x >= 0.9 and x <= 1.0 :
        return "A"
    elif x >= 0.8 :
        return "B"
    elif x >= 0.7 :
        return "C"
    elif x >= 0.6:
        return "D"
    elif x >= 0.0 and x < 0.6:
        return "F"
    

try:
    score = float(input("Enter a score between 1.0 and 0.0: "))
    print(letterGrade(score))
except:
    print("Please enter a numerical score")
