import random

print('Welcome to Hangman Game !')

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
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
lives = 6
word_list = ['apple', 'Tiger', 'Elephant', 'Dog', 'Banana']

chosen_word = random.choice(word_list).lower()
display = []

for _ in chosen_word:
    display += '_'
# print(f'The chosen word is {chosen_word}')
print(display)
end_of_game = False
while not end_of_game:
    user_input = input('Enter the letter : ')

    for i in range(len(chosen_word)):
        if user_input == chosen_word[i]:
            display[i] = chosen_word[i]
    if user_input not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You Lose')
    print(display)
    if '_' not in display:
        end_of_game = True
        print('You Win !')
    print(stages[lives])
