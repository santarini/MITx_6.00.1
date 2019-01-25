s = 'azcbobobegghakl'
alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
for letterInStr in range(0,len(s)):
    #take in a letter from a string
    s[letterInStr]
    #get letter's numeric index reference in alphabet list
    alphabetStart = alphabet.index(s[letterInStr])
    print(alphabetStart)
    #if the letter is Z next letter.
    if alphabetStart == 25:
        continue
    #if the next letter in the string is equal to the next letter index of alphabet reference
    if s[letterInStr + 1] == alphabet[alphabetStart + 1]:
        print("YEP")
        #increment counter
        #concat character to stringplace holder
        #reset index reference
        #check again
        #once cycle is broken push final string to list
    #return string of greatest length
