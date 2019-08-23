def count(word, letter):
    number = 0
    for index in word:
        if index == letter:
            number += 1
    return number

print(count('banana', 'a'))
