def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase
    for x in lettersGuessed:
        if x in alphabet:
            alphabet = alphabet.replace(str(x),'')
    
    return(alphabet)
