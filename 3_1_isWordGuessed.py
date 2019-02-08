def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secretWordLetters = []
    #take letters from word and put them in a list, remove duplicates
    for letter in secretWord:
        if letter not in secretWordLetters:
            secretWordLetters.append(letter)
    #check if all letters in word are in guess
    if all(letters in lettersGuessed for letters in secretWordLetters):
        return(True)
    else:
        return(False)
