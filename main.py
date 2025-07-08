import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)

# Display the first letter and underscores for the rest of the word
placeholder = chosen_word[0]  # Show the first letter
for position in range(1, len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = [chosen_word[0]]  # Since the first letter is already revealed

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue  # Skip the rest of the loop and prompt the user again

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If guess is incorrect, lose a life
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"============  IT WAS {chosen_word}! YOU LOSE :(  ============")

    # Check if user has guessed the word
    if "_" not in display:
        game_over = True
        print("============  YOU WIN! GG  ============")

    # Display the hangman stages corresponding to remaining lives
    print(stages[lives])
