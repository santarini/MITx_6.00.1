def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWordWithGuesses = ''
    secretWordLetters = []
    #take letters from word and put them in a list, remove duplicates
    for letter in secretWord:
        if letter not in secretWordLetters:
            secretWordLetters.append(letter)


    #secretWordLength = len(secretWord)
    for x in secretWord:
        #if character in secret word is in list add character
        if x in lettersGuessed:
            secretWordWithGuesses = secretWordWithGuesses + x
        #else add uderscore
        else:
            secretWordWithGuesses = secretWordWithGuesses + '_ '


    return(secretWordWithGuesses)
