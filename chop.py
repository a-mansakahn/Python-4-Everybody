def chop(list): #function def ends with a :
    cut = list[1:len(list)-1] #slice goes from the first index upto but not including the last index
    return None

def middle(list):
    return list[1:len(list)-1]

t = [1, 2, 3, 4, 5, 6]
chop(t)
print(middle(t))
