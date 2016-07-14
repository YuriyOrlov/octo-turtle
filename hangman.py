# Hangman game
#
'''
An example of a hangman game, created for practice purposes.
'''

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    listGuessed=[]
    for i in lettersGuessed:
        if i in secretWord:
            listGuessed.append(i)
    if len(listGuessed)==len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    listGuessed=''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            listGuessed+=secretWord[i]
        else:
            listGuessed+=' _ '
    return listGuessed


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not yet been guessed.
    '''
    
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabetMod=''
    for i in range(len(alphabet)):
        if alphabet[i] not in lettersGuessed:
           alphabetMod+=alphabet[i]
    return alphabetMod

def hangman(secretWord):
       
    print "Welcome to the game Hangman!"
    print ("I am thinking of a word that is " + str(len(secretWord))+ ' letters long')
    print ('-----------')
    lettersGuessed=[]
    mistakes=0

    while mistakes <8:
        availableLetters = getAvailableLetters(lettersGuessed)
        print ('You have '+str(8-mistakes)+' guesses left!')
        print ('Available Letters:' +availableLetters)
        
        guess= raw_input('Please guess a letter:')
        guess=guess.lower()
        
        if guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print ('-----------')
        elif guess in secretWord:
            lettersGuessed+= guess
            print('Good guess:'+ getGuessedWord(secretWord, lettersGuessed))
            print ('-----------')
            if isWordGuessed(secretWord, lettersGuessed)==True:
                break
        else:
            lettersGuessed+=guess
            mistakes+=1
            print ('Oops! That letter is not in my word: '+ getGuessedWord(secretWord, lettersGuessed))
            print ('-----------')
    win = isWordGuessed(secretWord, lettersGuessed)
    
    if win:
        print ('Congratulations, you won!')
    else:
        print ('Sorry, you run out of guesses. The word was '+secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
