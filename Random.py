import random
random_num = random.randint(0, 10)
print(random_num)
random_num_guess_correct = False
play_again = input("You will choose this later, press the enter key or put a random letter into this prompt: ")
rand_int_guess = int(input("Guess a numner from 0 to ten: "))
if rand_int_guess == random_num:
    print("You guessed the random number!")
    random_num_guess_correct = True
if random_num_guess_correct == True:
    play_again = input("Would you like to play again (y/n): ")
    if play_again == "y":
        random_num_guess_correct = False
        rand_int_guess = int(input("Guess a number from one to ten: "))
        random_num_two = random.randint(0, 10)
        if rand_int_guess == random_num_two:
            print("You guessed the right number")
    if play_again == "n":
        print("Goodbye: ")
if rand_int_guess != random_num:
    print("That was the wrong number")
if rand_int_guess > random_num:
    print("Your guess was too high")
if rand_int_guess < random_num:
    print("Your guess was too low")
