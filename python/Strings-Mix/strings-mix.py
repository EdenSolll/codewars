def mix(s1, s2):
    s1_letters = {}
    s2_letters = {}
    final_string = ''
    for letter in s1:
        if ord(letter) in range(97, 122):
            if letter in s1_letters:
                s1_letters[letter] += 1 
            else:
                s1_letters[letter] = 1 
    for letter in s2:
        if ord(letter) in range(97, 122):
            if letter in s2_letters:
                s2_letters[letter] += 1
            else:
                s2_letters[letter] = 1 
    print(s1_letters)
    print(s2_letters)
    sorteddi = (sorted(s1_letters.items(), key=lambda item: item[1]))
    sorteddict2 = (sorted(s2_letters.items(), key=lambda item: item[1]))

    for value in range(len(sorteddict1)):
        if sorteddict1[value] in sorteddict2 and sorteddict1[value] > sorteddict2[value] and sorteddict1[value] > 1:
   #        final_string += value * sorteddict1[value]
   #    if sorteddict1[value] > 1
    

string1=("Are they here")
string2=("yes, they are here")
print(mix(string1,string2))
