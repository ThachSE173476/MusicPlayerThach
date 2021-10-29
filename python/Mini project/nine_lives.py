import random

lives = 9
words =['pizza','fairy','teeth','shirt','otter','plane']
secret_word = random.choice(words)
clue = list('?'*len(secret_word))
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guess_letter, secrect_word, clue):
    index = 0
    while index < len(secrect_word):
        if guess_letter == secrect_word[index]:
            clue[index] = guess_letter
        index = index +1

while lives >0:
    print(clue)
    print('Lives left '+ heart_symbol*lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect, You lose a life')
        lives = lives -1 
    
if guessed_word_correctly:
    print('You won! The secret word was '+ secret_word)
else:
    print('You lost! The secret word was ' + secret_word)