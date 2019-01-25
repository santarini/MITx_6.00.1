s = 'azcbobobegghakl'
stringHolder = ""
orderCount = 0
orderExtracts = []
alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
for letterInStr in range(0,len(s)):
    #take in a letter from a string
    #push letter to string place holder 
    stringHolder = stringHolder + s[letterInStr]
    #get letter's numeric index reference in alphabet list
    alphabetStart = alphabet.index(s[letterInStr])
    print(alphabetStart)
    #if the letter is Z go to next letter.
    if alphabetStart == 25:
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
    #if the next letter in the string is equal to the next letter of alphabet list  
    if s[letterInStr + 1] == alphabet[alphabetStart + 1]:
        #increment orderCounter
        orderCount += 1
        #concat character to stringplace holder
        stringHolder = stringHolder + s[letterInStr]
        orderExtracts.append(stringHolder)
        #reset index reference
        #check again
        #once cycle is broken push final string to list
    else:
        orderExtracts.append(stringHolder)
        stringHolder = ""
    #return string of greatest length
print(orderExtracts)
