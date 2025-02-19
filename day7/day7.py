#Hangman
import random 
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
for _ in range(len(chosen_word)): 
    placeholder += '_'

print(placeholder)

game_over = False
correct_letters = []

while not game_over: 
    print("You have " + str(lives) + "/6 lives left!")
    guess = input("Guess a letter: ").lower()

    display = ''
    for letter in chosen_word: 
        if letter == guess: 
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters: 
            display += letter
        else: 
            display += "_"

    if guess not in chosen_word: 
        lives -= 1
        if lives == 0: 
            game_over = True
            print("You lose! The chosen word was " + chosen_word + ".")

    if "_" not in display: 
        game_over = True
        print("You win!")


    print(stages[lives])