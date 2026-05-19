import random 

words = ("python", "hangman", "programming", "challenge", "developer")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   "/  ",
                   "   "),
               3: (" o ",
                   "/ \\",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\ ")}


def display_hangman(wrong_guesses):
    print("________________________________")
    for line in hangman_art [wrong_guesses]:
        print(line)
    print("________________________________")



def display_hint(hint):
    print(" " .join(hint))
    

def display_answer(answer):
    print(" " .join(answer))

def main():
    answer = random.choice(words)
    print("Welcome to Hangman!")
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a Letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input. Only single letter is allower")
            continue
        if guess in guessed_letter:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letter.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("Congratulation You guessed the word.",)
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            # display_answer(answer)
            print(f"The Correct Word was: {answer}")
            print("Game Over!!! You LOST!!!")
            is_running = False



if __name__ == "__main__":
    main()




