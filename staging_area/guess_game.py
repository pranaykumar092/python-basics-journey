import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Guess any number between {lowest_num} to {highest_num}")

while is_running:

    guess = input("Enter a guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses +=1 

        if guess < lowest_num or guess > highest_num:
            print("This is not valid")
            print(f"Please select a number between {lowest_num} to {highest_num}")

        elif guess < answer:
            print("The guess is too low")

        elif guess > answer:
            print("The guess is too high")

        else:
            print(f"Correct!!! The number was {answer}")
            print(f"The number of guesses are {guesses}")
            is_running = False

    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_num} to {highest_num}")
        
                  

    

