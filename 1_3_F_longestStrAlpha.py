s = 'qiffuhbsjbesrxjpovlj'
stringHolder = ""
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
        #push it to the list
        orderExtracts.append(stringHolder)
        #Don't reset the string place holder
    else:
        orderExtracts.append(stringHolder)
        stringHolder = ""
    #return string of greatest length
#print(max(orderExtracts, key=len))
#docs for max https://docs.python.org/3/library/functions.html#max
#If multiple items are maximal, the function returns the first one encountered.
#So function already picks first winner in list for tie.
print("Longest substring in alphabetical order is: " + str(max(orderExtracts, key=len)))


#Failed. i didn't read the instructions well and ended up writing an algo that did something other than the task.
#But it was too much work to throw away so I'm keeping it.
