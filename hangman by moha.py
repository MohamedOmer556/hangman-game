import random
import time


print('Welcome to Hangman Game by Moha')
name = input('Enter Your Name Here\n')
print(f'hello {name}! Best of Luck')
time.sleep(2)
print('The game is about to start\n Lets Play Hangman!')
time.sleep(3)


def main():
    # Define the main function
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    words_to_guess = ["january", "border", "image", "film",
                      "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    display = '_' * length
    count = 0
    already_guessed = []
    play_game = ""

# loop to execute the game again


def play_loop():
    global play_game
    play_game = input('Do You Want to Play Again ? y = yes, n = no \n').lower()
    while play_game not in ['y', 'Y', 'n', 'N']:
        play_game = input(
            'Do You Want to Play Again ? y = yes, n = no \n').lower()
    if play_game == 'y':
        main()
    elif play_game == 'n':
        print('Thanks For Playing! We expect you back again!')
        exit()


def hangman():
    global display
    global already_guessed
    global word
    global count
    global play_game
    limit = 5

    guess = input(f'This is the Hangman Word: {display} Enter your guess: \n')
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
        print('Invalid Input, Try a letter\n')
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + '_' + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + '\n')

    elif guess in already_guessed:
        print('try differant letter.\n')

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print('|||||')
            print(f'wrong guess {str(limit - count)} guesses remainig')

        elif count == 2:
            time.sleep(1)
            print('>>>>>')
            print(f'wrong guess {str(limit - count)} guesses remainig')

        elif count == 3:
            time.sleep(1)
            print('......')
            print(f'wrong guess {str(limit - count)} guesses remainig')

        elif count == 4:
            time.sleep(1)
            print('??????')
            print(f'wrong guess {str(limit - count)} guesses remainig')

        elif count == 5:
            time.sleep(1)
            print('<<<<<<')
            print("Wrong guess. You are hanged!!!\n")
            print('Word is ', already_guessed, word)
            play_loop()

    if word == '_' * length:
        print('congratulations you won!')
        play_loop()


    elif count != limit:
        hangman()


main()

hangman()
