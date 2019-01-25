s = 'qiffuhbsjbesrxjpovlj'
stringHolder = ""
orderExtracts = []
alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
for letterInStr in range(0,len(s)):
    #take in a letter from a string
    #push letter to string place holder 
    stringHolder = stringHolder + s[letterInStr]
    #get letter's numeric index reference in alphabet list
    alphabetRef = alphabet.index(s[letterInStr])
    print(alphabetRef)
    #if the letter is Z go to next letter.
    if alphabetRef == 25:
        #push the string holder to the extract list
        orderExtracts.append(stringHolder)
        #reset the string
        stringHolder = ""
        continue
    #if this is the last letter in s then continue
    if letterInStr == len(s)-1:
        #push the string holder to the extract list
        orderExtracts.append(stringHolder)
        #reset the string
        stringHolder = ""
        continue
    #if the next letter in s has a greater alphabet reference
    if s[letterInStr + 1] >= alphabet[alphabetRef]:
        print("YEP")
        orderExtracts.append(stringHolder)
    else:
        orderExtracts.append(stringHolder)
        stringHolder = ""
print("Longest substring in alphabetical order is: " + str(max(orderExtracts, key=len)))

