def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    #define some things
    lettersGuessed = []
    #intro prompt
    print("Welcome to the game, Hangman!")
    turnCount = 1
    #tell the user how many letter are in their word
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    while turnCount <= 8:
        print("-------------")
        print("You have " + str(9-turnCount) + " guesses left.")
        #print available letters
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available letters: " + availableLetters)
        #ask the user to supply a letter
        guess = input("Please guess a letter: ")
        #if guess has been guessed before
        if guess in lettersGuessed:
            secretWordStatus = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter: " + secretWordStatus)
            continue
        else:
            lettersGuessed.append(guess)
        #get secretword with guesses
        secretWordStatus = getGuessedWord(secretWord, lettersGuessed)
        #if guess is in word
        if guess in secretWord:
            print("Good guess: " + secretWordStatus)
        #if guess is NOT in word
        if not(guess in secretWord):
            turnCount += 1
            print("Oops! That letter is not in my word: " + secretWordStatus)
        #check if player won
        winCondition = isWordGuessed(secretWord, lettersGuessed)
        if winCondition == True:
            print("-------------")
            print("Congratulations, you won!")
            break
        #print(turnCount)
    if turnCount > 8:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was else.")
