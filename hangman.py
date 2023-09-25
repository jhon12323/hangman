import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# word_list = ["elephant","peacock","lion","tiger"]
from hangman_words import word_list

choosen_word = (random.choice(word_list))
print(choosen_word)

lives = 6

display=[]
for letter in choosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:

    user = input("Guess a random letter: ").lower()

    for i in range (len(choosen_word)):
        position = choosen_word[i]
        if position == user:
            display[i] = position
    print(display)

    if user not in choosen_word:
        lives -= 1
        if lives == 0:
          end_of_game = True
          print("You lose!")

    if "_" not in display:
        end_of_game = True

        print("You win!")
    
    print(stages[lives])

   
    
   
  
        
   






